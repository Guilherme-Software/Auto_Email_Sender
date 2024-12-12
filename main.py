import schedule
import time
import os
import smtplib
from email.message import EmailMessage
#Config Email and password
EMAIL_ADRESS = 'your_gmail.com'
EMAIL_PASSWORD = 'your_password'

#create an email
def Emailsending():
    msg = EmailMessage()
    msg['Subject'] = 'title'
    msg['From'] = EMAIL_ADRESS
    msg['To'] = 'other_person@gmail.com'
    msg.set_content('mesage that you want')

#send an email
    try:

        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        print("Email sent successfully!")
    except Exception as e:
            print(f"error sending email: {e}")


#schedule.what.day/time.do
schedule.every(24).hours.do(Emailsending)

while 1:
    schedule.run_pending()
    time.sleep(1)
