# -*- coding=utf-8 -*-
"""
    通过IMAP协议查收远程服务器中的电子邮件。
"""
import argparse
import getpass
import imaplib

GOOGLE_IMAP_SERVER = 'imap.googleemail.com'


def check_email(username):
    mailbox = imaplib.IMAP4_SSL(GOOGLE_IMAP_SERVER, '993')
    password = getpass.getpass(prompt='Password: ')
    mailbox.login(username, password)
    mailbox.select('Inbox')

    typ, data = mailbox.search(None, 'ALL')
    for num in data[0].split():
        typ, data = mailbox.fetch(num, '(RFC822)')
        print("Message %s\n%s\n" % (num, data[0][1]))
        break
    mailbox.close()
    mailbox.logout()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Email Download Example")
    parser.add_argument('--username', action="store", dest="username", default=getpass.getuser())

    given_args = parser.parse_args()
    username = given_args.username
    check_email(username)
