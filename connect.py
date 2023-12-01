import smtplib
import credentials

def sendEmails(pairs: list, emails: dict):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(credentials.FROM, credentials.appPassword)
    for Santa, Secret in pairs:
        message = f'''Subject: Secret Santa 2023\n\nWelcome to the Homies with X Chromies 3rd annual secret santa! Thank you for participating {Santa}! Before I tell you who you are buying for, let me remind you of the rules.
        1) $25 spending limit
        2) You may not tell anyone else who you are buying for
        3) This year, you may need to mail it to the recipient, so their address will be included if that is needed.
        4) You cannot buy for your s/o. This should already be implemented but if you recieve your s/o please let the groupchat know so that can be addressed.
        
Now for the big reveal! You will be purchasing for {Secret}! Their interests include {emails[Secret]["interests"]}. Their address is {emails[Secret]["address"]}.
        
Have fun and see you soon!'''
        target = emails[Santa]["email"]
        s.sendmail(credentials.FROM, target, message)
    s.quit()
