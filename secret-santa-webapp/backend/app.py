from flask import Flask, request, jsonify
from flask_cors import CORS
import random
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from card_templates import generate_email_card

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Add logging for debugging
@app.before_request
def log_request():
    print(f"Received {request.method} request to {request.path}")
    if request.method == 'POST':
        print(f"Request data: {request.get_json()}")


def create_secret_santa_list(names, excluded_pairings=None):
    """
    Generate Secret Santa pairings with exclusion rules.
    Based on the original Python implementation.
    """
    if excluded_pairings is None:
        excluded_pairings = {}

    random.seed(datetime.now().timestamp())
    secret_santa_list = []
    remaining_names = names.copy()

    for giver in names:
        possible_recipients = [
            name for name in remaining_names
            if name != giver and name not in excluded_pairings.get(giver, [])
        ]

        if not possible_recipients:
            # If there are no valid recipients, start over
            return create_secret_santa_list(names, excluded_pairings)

        recipient = random.choice(possible_recipients)
        secret_santa_list.append((giver, recipient))
        remaining_names.remove(recipient)

    return secret_santa_list


def send_email(smtp_config, recipient_email, subject, html_body):
    """Send an HTML email using SMTP."""
    try:
        s = smtplib.SMTP(smtp_config['server'], smtp_config['port'])
        s.starttls()
        s.login(smtp_config['email'], smtp_config['password'])

        msg = MIMEMultipart('alternative')
        msg['From'] = smtp_config['email']
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach HTML content
        msg.attach(MIMEText(html_body, 'html'))

        s.send_message(msg)
        s.quit()
        return True
    except Exception as e:
        raise Exception(f"Failed to send email to {recipient_email}: {str(e)}")


@app.route('/api/send', methods=['POST'])
def send_secret_santa():
    """
    Main endpoint to generate pairings and send emails.
    In non-test mode, pairings are never returned to the client.
    """
    try:
        data = request.json

        # Debug logging
        print(f"Received request - testMode: {data.get('testMode', False)}")

        participants = data.get('participants', [])
        exclusions = data.get('exclusions', {})
        email_subject = data.get('emailSubject', 'Secret Santa')
        email_template = data.get('emailTemplate', '')
        smtp_config = data.get('smtpConfig', {})
        card_style = data.get('cardStyle', 'classic')
        test_mode = data.get('testMode', False)
        email_debug_mode = data.get('emailDebugMode', False)

        # Validate input
        if len(participants) < 3:
            return jsonify({'error': 'Need at least 3 participants'}), 400

        # Only validate SMTP config if NOT in test mode
        if not test_mode:
            if not smtp_config:
                return jsonify({'error': 'SMTP configuration required for real send mode'}), 400
            if not smtp_config.get('email') or not smtp_config.get('password'):
                return jsonify({'error': 'SMTP email and password required for real send mode'}), 400

        # Extract names for pairing algorithm
        names = [p['name'] for p in participants]

        # Create participant lookup dictionary
        participant_dict = {p['name']: p for p in participants}

        # Generate pairings
        pairings = create_secret_santa_list(names, exclusions)

        # Test mode: return pairings without sending emails
        if test_mode:
            pairing_results = [
                {'giver': giver, 'recipient': recipient}
                for giver, recipient in pairings
            ]
            return jsonify({
                'success': True,
                'testMode': True,
                'pairings': pairing_results
            })

        # Send emails (pairings are not returned to client)
        emails_sent = 0
        errors = []

        for giver_name, recipient_name in pairings:
            giver = participant_dict[giver_name]
            recipient = participant_dict[recipient_name]

            # Replace template variables in message body
            message_body = email_template
            message_body = message_body.replace('{giver_name}', giver['name'])
            message_body = message_body.replace('{recipient_name}', recipient['name'])
            message_body = message_body.replace('{recipient_interests}', recipient['interests'])
            message_body = message_body.replace('{recipient_address}', recipient.get('address', ''))

            # Generate HTML email card
            html_body = generate_email_card(
                card_style,
                giver['name'],
                recipient['name'],
                recipient['interests'],
                recipient.get('address', ''),
                message_body
            )

            try:
                # If email debug mode is enabled, send to the sender's email instead of the recipient
                target_email = smtp_config['email'] if email_debug_mode else giver['email']
                send_email(smtp_config, target_email, email_subject, html_body)
                emails_sent += 1
            except Exception as e:
                errors.append(str(e))

        if errors:
            return jsonify({
                'success': False,
                'error': 'Some emails failed to send',
                'details': errors,
                'emailsSent': emails_sent
            }), 500

        return jsonify({
            'success': True,
            'emailsSent': emails_sent
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """Simple health check endpoint."""
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    # Use port 5001 to avoid conflict with macOS AirPlay on port 5000
    app.run(debug=True, port=5001)
