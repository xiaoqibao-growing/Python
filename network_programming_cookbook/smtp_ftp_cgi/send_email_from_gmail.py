# -*- coding=utf-8 -*-
"""
    通过Gmail的SMTP服务器发送带有附件的电子邮件。
"""
import argparse
import os
import getpass
import re
import sys
import smtplib

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.gmai.com'
SMTP_PORT = 587


def send_email(sender, recipient):
    """ Send email message """
    msg = MIMEMultipart()
    msg['Subject'] = 'Python Email Test'
    msg['To'] = recipient
    msg['From'] = sender
    subject = 'Python email test'
    message = 'Images attached'

    # attach image files
    files = os.listdir()
    gifsearch = re.compile(".gif", re.IGNORECASE)
    files = filter(gifsearch.search, files)

    for filename in files:
        path = os.path.join(os.getcwd(), filename)
        if not os.path.isfile(path):
            continue
        img = MIMEImage(open(path, 'rb').read(), _subtype="gif")
        img.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(part)

    part = MIMEText('text', 'plain')
    part.set_payload(message)
    msg.attach(part)

    # Create smtp session
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo
    password = getpass.getpass(prompt='Password: ')
    session.login(sender, password)
    session.sendmail(sender, recipient, msg.as_string())
    print("Email sent")
    session.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Email Sending Example")
    parser.add_argument('--sender', action="store", dest="sender")
    parser.add_argument('--recipient', action="store", dest="recipient")

    given_args = parser.parse_args()
    send_email(given_args.sender, given_args.recipient)
