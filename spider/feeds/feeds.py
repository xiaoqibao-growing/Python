'''#! /usr/bin/env python'''
# coding=utf-8

import requests
import multiprocessing

from Queue import Queue
from bs4 import BeautifulSoup


class FeedSpider(object):
    def __init__(self, url):
        self.url = url
        self.url_pool = []

    def fetch_url(self, html):
        soup = BeautifulSoup(html, "lxml")

        for item in soup.find_all("a"):
            self.url_pool.append("http://osint.bambenekconsulting.com" + item.get("href"))

    def fetch_data(self, url):
        response = requests.get(url)
        print response.text


if __name__ == '__main__':
    feed_spider = FeedSpider("http://osint.bambenekconsulting.com/feeds/")

    response = requests.get(feed_spider.url)
    feed_spider.fetch_url(response.text)

    # print feed_spider.url_pool.qsize()
    # feed_spider.url_pool.get()
    # print feed_spider.url_pool.qsize()

    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    pool.map(feed_spider.fetch_data, feed_spider.url_pool)
