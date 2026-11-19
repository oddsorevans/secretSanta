import os
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import Flask, request, jsonify
from flask_cors import CORS

from card_templates import render_card, fill_template, theme_list

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

MAX_ATTEMPTS = 10000
_rng = random.SystemRandom()


def create_secret_santa_list(names, excluded_pairings=None):
    """Return [(giver, recipient)] honoring exclusions. Shuffle until valid so
    every valid assignment is equally likely. Raises ValueError if none found."""
    excluded = excluded_pairings or {}
    recipients = list(names)
    for _ in range(MAX_ATTEMPTS):
        _rng.shuffle(recipients)
        if all(g != r and r not in excluded.get(g, []) for g, r in zip(names, recipients)):
            return list(zip(names, recipients))
    raise ValueError('No valid pairing found - loosen the exclusions')


def parse_participants(raw, need_email):
    """Strip/validate participants. Raises ValueError with a user-facing message."""
    people = []
    for p in raw or []:
        person = {k: str(p.get(k, '')).strip() for k in ('name', 'email', 'interests', 'address')}
        if not person['name']:
            raise ValueError('Every participant needs a name')
        if need_email and not person['email']:
            raise ValueError(f"{person['name']} has no email address")
        people.append(person)
    if len(people) < 3:
        raise ValueError('Need at least 3 participants')
    if len({p['name'] for p in people}) != len(people):
        raise ValueError('Participant names must be unique')
    return people


def build_message(sender, to, subject, html):
    msg = MIMEMultipart('alternative')
    msg['From'], msg['To'], msg['Subject'] = sender, to, subject
    # plain-text first, HTML last (clients prefer the last part)
    msg.attach(MIMEText('This Secret Santa card needs an HTML-capable email client.', 'plain'))
    msg.attach(MIMEText(html, 'html'))
    return msg


@app.route('/api/themes')
def themes():
    return jsonify(theme_list())


@app.route('/api/preview', methods=['POST'])
def preview():
    data = request.get_json(silent=True) or {}
    giver = data.get('giver') or {}
    recipient = data.get('recipient') or {}
    return jsonify({'html': render_card(
        data.get('cardStyle'),
        {'name': str(giver.get('name', ''))},
        {k: str(recipient.get(k, '')) for k in ('name', 'interests', 'address')},
        str(data.get('emailTemplate', '')),
    )})


@app.route('/api/send', methods=['POST'])
def send_secret_santa():
    """Generate pairings; in test mode return cards, otherwise email them.
    Real-send responses never contain pairings."""
    data = request.get_json(silent=True) or {}
    test_mode = bool(data.get('testMode'))
    smtp = data.get('smtpConfig') or {}
    subject = data.get('emailSubject') or 'Secret Santa'
    template = data.get('emailTemplate', '')
    style = data.get('cardStyle')

    try:
        people = parse_participants(data.get('participants'), need_email=not test_mode)
        if not test_mode and not (smtp.get('email') and smtp.get('password')):
            raise ValueError('SMTP email and password required for real send mode')
        by_name = {p['name']: p for p in people}
        pairings = create_secret_santa_list([p['name'] for p in people], data.get('exclusions') or {})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    def card(giver, recipient):
        return render_card(style, giver, recipient, template)

    if test_mode:
        return jsonify({'success': True, 'testMode': True, 'pairings': [
            {'giver': g, 'recipient': r, 'giverEmail': by_name[g]['email'],
             'html': card(by_name[g], by_name[r])}
            for g, r in pairings
        ]})

    sent, failed = 0, []
    try:
        with smtplib.SMTP(smtp.get('server') or 'smtp.gmail.com', int(smtp.get('port') or 587), timeout=30) as s:
            s.starttls()
            s.login(smtp['email'], smtp['password'])  # fail before sending anything
            for g, r in pairings:
                # email debug mode: everything goes to the organizer
                to = smtp['email'] if data.get('emailDebugMode') else by_name[g]['email']
                try:
                    s.send_message(build_message(smtp['email'], to, subject, card(by_name[g], by_name[r])))
                    sent += 1
                except smtplib.SMTPException:
                    failed.append(g)  # names the giver only; the pairing stays secret
    except (smtplib.SMTPException, OSError) as e:
        return jsonify({'error': f'SMTP error: {e}', 'emailsSent': sent, 'failed': failed}), 502

    return jsonify({'success': not failed, 'emailsSent': sent, 'failed': failed})


@app.route('/api/health')
def health_check():
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    # Port 5001 avoids macOS AirPlay on 5000. Debug only via FLASK_DEBUG=1.
    app.run(debug=os.environ.get('FLASK_DEBUG') == '1', port=5001)
