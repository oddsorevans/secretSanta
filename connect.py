import smtplib
import credentials

def sendEmails(pairs: dict, emails: dict):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(credentials.FROM, credentials.appPassword)
    for key in pairs:
        value = pairs[key]
        message = f'''Subject: Secret Santa 2022\n\nWelcome to the Homies with X Chromies 2nd annual secret santa! Thank you for participating {key}! Before I tell you who you are buying for, let me remind you of the rules.
        1) $20 spending limit
        2) You may not tell anyone else who you are buying for
        3) Gifts will all be exchanged on a TBD date. Check group chat for updates
        4) You cannot buy for your s/o. This should already be implemented but if you recieve your s/o please let the groupchat know so that can be addressed.
        
Now for the big reveal! You will be purchasing for {value}! Their interests include {emails[value]["interests"]}.
        
Have fun and see you soon!'''
        target = emails[key]["email"]
        s.sendmail(credentials.FROM, emails[key]["email"], message)
    s.quit()


illegal = {
    "Dylan":"Rachel",
    "Rachel":"Dylan",
    "Chris":"Sarah",
    "Sarah":"Chris",
    "Ron":"Sydney",
    "Sydney":"Ron"
}
