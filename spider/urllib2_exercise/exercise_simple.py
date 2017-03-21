# -*- coding:utf-8 -*-
# __author__ = xuejun
import urllib2


def simple_1():
    response = urllib2.urlopen('http://www.baidu.com')
    html = response.read()
    print(html)


def simple_2():
    request = urllib2.Request('http://www.baidu.com')
    response = urllib2.urlopen(request)

    return response.read()


def simple_3():
    request = urllib2.Request('http://bbs.csdn.net/callmewhy')

    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError as he:
        print("The server could not fulfill the request")
        print(he.code)
    except urllib2.URLError as ue:
        print("We failed to reach a server.")
        print(ue.reason)
    else:
        return response.read()


def simple_4():
    request = urllib2.Request('http://bbs.csdn.net/callmewhy')

    try:
        response = urllib2.urlopen(request)
    except urllib2.URLError as ue:
        if hasattr(ue, 'reason'):
            print("We failed to reach a server.")
            print(ue.reason)
        elif hasattr(ue, 'code'):
            print("The server could not fulfill the request")
            print(he.code)
    else:
        return response.read()


def simple_5():
    # Create a manager fo password.
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    top_level_url = "http://example.com/foo/"
    # Add username and password.
    password_mgr.add_password(None, top_level_url, 'why', '123')

    # Create a handler.
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)

    opener = urllib2.build_opener(handler)
    a_url = 'http://www.baidu.com'
    opener.open(a_url)

    urllib2.install_opener(opener)


def simple_6():
    enable_proxy = True
    proxy_handler = urllib2.ProxyHandler({'http': 'http://some-proxy.com:8080'})
    null_proxy_handler = urllib2.ProxyHandler({})

    if enable_proxy:
        opener = urllib2.build_opener(proxy_handler)
    else:
        opener = urllib2.build_opener(null_proxy_handler)

    urllib2.build_opener(opener)


def simple_7():
    import cookielib

    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open('http://www.baidu.com')
    for item in cookie:
        print(item.name)


def simple_8():
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    httpsHandler = urllib2.HTTPSHandler(debuglevel=1)

    opener = urllib2.build_opener(httpHandler, httpsHandler)
    urllib2.install_opener(opener)
    response = urllib2.urlopen('http://www.baidu.com')


def simple_9():
    import urllib
    postdata = urllib.urlencode(
        {
            'username': 'python',
            'password': 'why124',
            'continueURI': 'http:..www.verycd.com',
            'fk': '',
            'login_submit': '登录',
        }
    )

    request = urllib2.Request(
        url= 'http://secure.verycd.com/signin',
        data = postdata
    )

    result = urllib2.urlopen(request)

    print(result.read())


def simple_10():
    import urllib
    postdata = urllib.urlencode(
        {
            'username': 'python',
            'password': 'why124',
            'continueURI': 'http:..www.verycd.com',
            'fk': '',
            'login_submit': '登录',
        }
    )

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
        'Referer': 'http://www.cnbeta.com/article',
    }

    request = urllib2.Request(
        url='http://secure.verycd.com/signin',
        data=postdata,
        headers=headers,
    )

    result = urllib2.urlopen(request)

    print(result.read())


if __name__ == '__main__':
    # simple_1()
    # print(simple_2())
    # print(simple_4())
    simple_8()
