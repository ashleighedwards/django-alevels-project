import email
import smtplib
import sqlite3
connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()
cursor.execute("SELECT first_name,email FROM auth_user")
email_and_usernames = cursor.fetchall()
from_email = "project-send123@outlook.com"
password = "passwordsender123"
for i in range(len(email_and_usernames)):
    for a in range(0,len(email_and_usernames[i]),2):
        name = email_and_usernames[i][a]
        msg = email.message_from_string("Hi "+str(name)+",\n This is a reminder to update the website for this week's item handouts. \n Thank you.")
        to_email = email_and_usernames[i][a-1]
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = "Victim Support Item Reminder"
        s = smtplib.SMTP("smtp.live.com",587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(from_email, password)
        s.sendmail(from_email, to_email, msg.as_string())
s.quit()
