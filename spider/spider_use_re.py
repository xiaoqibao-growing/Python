# -*- coding:utf-8 -*-
# __author__ = xuejun
# import urllib
# import urllib2
import requests
from time import time
import re

url = 'https://movie.douban.com/top250'


def fetch_page(url_path):
    response = requests.get(url_path)

    return response


def parse(url_path):
    response = fetch_page(url_path)
    page = response.content

    fetch_list = set()
    result = []

    for title in re.findall(r'<a href=.*\s.*<span class="title">(.*)</span>', page):
        result.append(title)

    for postfix in re.findall(r'<a href="(\?start=.*?)"', page):
        fetch_list.add(url_path + postfix.decode())

    for url_item in fetch_list:
        response = fetch_page(url_item)
        page = response.content

        for title in re.findall(r'<a href=.*\s.*<span class="title">(.*)</span>', page):
            result.append(title)

    for i, title in enumerate(result, 1):
        # title = title.decode()
        print(title)


def main():
    start = time()
    for i in range(5):
        parse(url)
    end = time()

    print('Cost {} seconds.'.format((start - end) / 5))

if __name__ == '__main__':
    main()
