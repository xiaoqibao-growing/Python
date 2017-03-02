# -*- coding:utf-8 -*-
# __author__ = xuejun
# import urllib
# import urllib2
import requests
import ssl
from lxml import etree

url = 'https://movie.douban.com/top250'
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)


def fetch_page(url_path):
    # request = urllib2.Request(url_path)
    # response = urllib2.urlopen(request)
    response = requests.get(url_path)

    return response


def parse(url_path):
    response = fetch_page(url_path)
    # page = response.read()  # urllib2
    page = response.content  # requests
    html = etree.HTML(page)

    xpath_movie = '//*[@id="content"]/div/div[1]/ol/li'
    xpath_title = './/span[@class="title"]'
    xpath_pages = './/*[@id="content"]/div/div[1]/div[2]/a'

    pages = html.xpath(xpath_pages)
    fetch_list = []
    result = []

    for element_movie in html.xpath(xpath_movie):
        result.append(element_movie)

    for p in pages:
        fetch_list.append(url_path + p.get('href'))

    for url_item in fetch_list:
        response = fetch_page(url_item)
        # page = response.read()
        page = response.content
        html = etree.HTML(page)

        for element_movie in html.xpath(xpath_movie):
            result.append(element_movie)

    for i, movie in enumerate(result, 1):
        title = movie.find(xpath_title).text
        print(title)


if __name__ == '__main__':
    parse(url)
