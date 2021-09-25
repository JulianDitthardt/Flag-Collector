import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage
import pandas as pd


class emailSender():
    def __init__(self):
        load_dotenv()
        self._emailAddress = os.environ.get("EMAIL_ADDRESS")
        self._emailPassword = os.environ.get("EMAIL_PASSWORD")

    def _createMessage(self,country):
        with open('emailTemplate.txt','r') as template:
            message = template.read().replace("{country}",country)
        return message

    def _sendEmail(self,country):
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(self._emailAddress,self._emailPassword)

            subject = "Interest in a copy of the flag."



if __name__ == '__main__':
    a = emailSender()
    print(a._createMessage("Bulgaria"))

# load_dotenv()
#
# email_address = os.environ.get("gmail_user")
# password = os.environ.get("gmail_password")
#
# with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
#
#     smtp.login(email_address,password)
#
#     subject = "Test"
#     body = "Is this working"
#
#     msg = f"Subject: {subject}\n\n{body}"
#
#     smtp.sendmail(email_address,"julian.ditthardt@y7mail.com",msg)