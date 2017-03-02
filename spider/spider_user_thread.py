# -*- coding:utf-8 -*-
# __author__ = xuejun
# import urllib
# import urllib2
import requests
from lxml import etree
from time import time
from threading import Thread

url = 'https://movie.douban.com/top250'


def fetch_page(url_path):
    response = requests.get(url_path)

    return response


def parse(url_path):
    response = fetch_page(url_path)
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
        print(p.get('href'))

    def fetch_content(_url):
        response = fetch_page(_url)
        # page = response.read()
        page = response.content
        html = etree.HTML(page)

        for element_movie in html.xpath(xpath_movie):
            result.append(element_movie)

    threads = []
    for url in fetch_list:
        t = Thread(target=fetch_content, args=[url])
        t.start()
        threads.append(t)

    for t in threads:  # 校验线程是否结束
        t.join()

    for i, movie in enumerate(result, 1):
        title = movie.find(xpath_title).text
        print(title)


def main():
    start = time()
    for i in range(5):
        parse(url)
    end = time()

    print('Cost {} seconds.'.format((start - end) / 5))

if __name__ == '__main__':
    main()
