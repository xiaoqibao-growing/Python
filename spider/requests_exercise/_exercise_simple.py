# -*- coding:utf-8 -*-
# __author__ = xuejun
import requests


def simple_1():
    """
    You can use these method below to request a url.
    :return:
    """
    r = requests.get('https://github.com/timeline.json')
    # r = requests.post("http://httpbin.org/post")
    # r = requests.put("http://httpbin.org/put")
    # r = requests.delete("http://httpbin.org/delete")
    # r = requests.head("http://httpbin.org/get")
    # r = requests.options("http://httpbin.org/get")
    return r.text


def simple_2():
    """
    Of course, you can transfer parameters.
    :return:
    """
    # payload = {'key1': 'value1', 'key2': 'value2'}
    # r = requests.get('http://httpbin.org/get', params=payload)
    # http://httpbin.org/get?key2=value2&key1=value1

    payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
    r = requests.get('http://httpbin.org/get', params=payload)
    # http: // httpbin.org / get?key2 = value2 & key2 = value3 & key1 = value1

    return r.url


def simple_3():
    """
    Also, you can transfer json and receive json.
    :return:
    """
    r = requests.get('https://github.com/timeline.json')
    return r


def simple_4():
    """
    You can also transfer file.
    :return:
    """
    url = 'http://httpbin.org/post'
    files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}

    r = requests.post(url, files=files)
    return r


def simple_5():
    """
    Get status of requests.
    :return:
    """
    r = requests.get('http://httpbin.org/get')
    # requests.codes.ok
    return r


if __name__ == '__main__':
    # print(simple_1())
    # print(simple_2())
    print(simple_5().status_code)
