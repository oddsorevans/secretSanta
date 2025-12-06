import smtplib
import credentials
from email.mime.text import MIMEText

def sendEmails(pairs: list, emails: dict):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(credentials.FROM, credentials.appPassword)
    for Santa, Secret in pairs:
        message = f'''Welcome to our 3rd Annual Secret Santa! Thank you for participating {Santa}! Before I tell you who you are buying for, let me remind you of the rules.
        1) $25 spending limit
        2) Remember, its a secret!
        3) These will be given out at the Christmas Party on December 26th at Evan's house!
        4) You cannot buy for your s/o. This shouldn't happen, but if you recieve your s/o please let Evan know so we can reroll.

Now for the big reveal! You will be purchasing for {Secret}! Their interests include {emails[Secret]["interests"]}.

Their address is: {emails[Secret]["address"]}

Have fun and see you soon!'''
        msg = MIMEText(message)
        msg['Subject'] = 'Friends Secret Santa 2024'
        target = emails[Santa]["email"]
        s.sendmail(credentials.FROM, target, msg.as_string())
    s.quit()
