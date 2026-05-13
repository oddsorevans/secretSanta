import os
import smtplib
from email.mime.text import MIMEText

try:
    import credentials
    SMTP_USER = credentials.FROM
    SMTP_PASSWORD = credentials.appPassword
except ImportError:
    SMTP_USER = os.environ.get('SECRET_SANTA_EMAIL')
    SMTP_PASSWORD = os.environ.get('SECRET_SANTA_APP_PASSWORD')


SUBJECT = os.environ.get('SECRET_SANTA_SUBJECT', 'Secret Santa')


def build_message(giver, recipient, recipient_info):
    return f'''Hi {giver}, thanks for participating in Secret Santa!

You will be purchasing for {recipient}.

Their interests include: {recipient_info["interests"]}

Their address is: {recipient_info["address"]}

Have fun!'''


def send_emails(pairs, participants, smtp_server='smtp.gmail.com', smtp_port=587):
    if not SMTP_USER or not SMTP_PASSWORD:
        raise RuntimeError(
            'SMTP credentials missing. Either create credentials.py from credentials.py.example '
            'or set SECRET_SANTA_EMAIL and SECRET_SANTA_APP_PASSWORD environment variables.'
        )

    s = smtplib.SMTP(smtp_server, smtp_port)
    s.starttls()
    s.login(SMTP_USER, SMTP_PASSWORD)
    try:
        for giver, recipient in pairs:
            msg = MIMEText(build_message(giver, recipient, participants[recipient]))
            msg['Subject'] = SUBJECT
            msg['From'] = SMTP_USER
            msg['To'] = participants[giver]['email']
            s.sendmail(SMTP_USER, participants[giver]['email'], msg.as_string())
    finally:
        s.quit()
