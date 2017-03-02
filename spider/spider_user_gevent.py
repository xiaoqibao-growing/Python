# -*- coding:utf-8 -*-
# __author__ = xuejun
import requests
from lxml import etree
from time import time
import gevent
from gevent import monkey

url = 'https://movie.douban.com/top250'


def fetch_page(url_path):
    response = requests.get(url_path)

    return response


def fetch_content(_url):
    response = fetch_page(_url)
    page = response.content
    return page


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

    jobs = [gevent.spawn(fetch_content, url) for url in fetch_list]
    gevent.joinall(jobs)
    # [job.value for job in jobs]

    for page in [job.value for job in jobs]:
        html = etree.HTML(page)

        for element_movie in html.xpath(xpath_movie):
            result.append(element_movie)

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
