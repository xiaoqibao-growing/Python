# -*- coding=utf-8 -*-

import urllib2

BROWSER = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
URL = 'http://www.python.org'


def spoof_firefox():
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', BROWSER)]

    result = opener.open(URL)
    print("Response headers:")
    for header in result.headers.headers:
        print("\t %s" % header)


if __name__ == '__main__':
    spoof_firefox()
