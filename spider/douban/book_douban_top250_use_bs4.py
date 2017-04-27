# coding=utf-8
"""
    本程序使用requests库和bs4库实现爬取豆瓣图书top250.
"""
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ProcessPoolExecutor


class Spider(object):
    def __init__(self, headers=None, cookie=None):
        self.headers = headers
        self.cookie = cookie
        self.result = []
        self.fetch_list = []

    def get_content(self, url):
        content = requests.get(url)
        content = content.text.strip()

        return content

    def get_content_by_regex(self, start):
        url = "https://book.douban.com/top250?start=" + str(start)
        content = self.get_content(url)
        soup = BeautifulSoup(content, "html.parser")

        for item in soup.find_all("table", width="100%"):
            div_ = item.find_all("div")
            author_p = item.find_all("p")
            print(author_p[0].string.encode("utf-8"))
            print(author_p[1].find("span").string.encode("utf-8"))
            for _ in div_:
                a_ = _.find_all("a")
                if a_:
                    print(a_[0].attrs['title'].encode("utf-8"))


    def go(self):
        """
            这里有个问题就是每次都是不同的实例，不能把数据保存到result中，除非设置全局变量。
        """
        with ProcessPoolExecutor(max_workers=4) as executor:
            executor.map(self, [index for index in range(0, 250, 25)])

    def __call__(self, start):
        return self.get_content_by_regex(start)

if __name__ == '__main__':
    spider = Spider()
    spider.go()
