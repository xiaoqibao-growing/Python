# -*- coding=utf-8 -*-
import ftplib

FTP_SERVER_URL = 'ftp.kernel.org'


def test_ftp_connection(path, username, email):
    # Open ftp connection
    frp = ftplib.FTP(path, username, email)

    # List the files in the /pub directory
    ftp.cwd("/pub")
    print("File list at %s:" % path)

    files = ftp.dir()
    print(files)

    ftp.quit()


if __name__ == '__main__':
    test_ftp_connection(path=FTP_SERVER_URL, username="anoymous", email='nobody@nourl.com')
