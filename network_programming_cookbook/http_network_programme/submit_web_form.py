# -*- coding=utf-8 -*-

import requests
import urllib
import urllib2

ID_USERNAME = 'signup-user-name'
ID_EMAIL = 'signup-user-email'
ID_PASSWORD = 'signup-user-password'
USERNAME = 'hahaha'
EMAIL = 'xj174850@163.com'
PASSWORD = 'yourpassword'
SIGNUP_URL = 'https://twitter.com/account/create'


def submit_form():
    """ Submit a form """
    payload = {
        ID_USERNAME : USERNAME,
        ID_EMAIL : EMAIL,
        ID_PASSWORD : PASSWORD,
    }

    # Make a get request
    resp = request.get(SIGNUP_URL)
    print("Headers from a POST request response: %s" % resp.headers)
    # print("HTML Response: %s" % resp.read())


if __name__ == '__main__':
    submit_form()
