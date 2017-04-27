# coding=utf-8
"""
    本程序使用requests库和re库实现爬取豆瓣图书top250.
"""
import requests
import re
import multiprocessing


class Spider(object):
    def __init__(self, headers=None, cookie=None):
        self.headers = headers
        self.cookie = cookie
        self.result = []
        self.fetch_list = []

    def get_content(self, url):
        content = requests.get(url)
        content = content.text.encode('utf-8')

        return content

    def get_content_by_regex(self, start):
        url = "https://book.douban.com/top250?start=" + str(start)
        content = self.get_content(url)

        regex = '<table width=\"100%\">.*?<div.*?<a.*?>(.*?)</a>.*?'\
            '</div>.*?<p.*?>(.*?)</p>.*?'\
            '<div.*?class=\"rating_nums\">(.*?)</span>.*?\((.*?)\).*?'\
            'class=\"inq\">(.*?).*?</table>'

        pattern = re.compile(regex, re.S)
        _ = re.findall(pattern, content)

        for item in _:
            #  这里可以把数据存放到mongodb中
            print(item[0].strip())
            self.result.append(item)

    def go(self):
        """
            这里有个问题就是每次都是不同的实例，不能把数据保存到result中，除非设置全局变量。
        """
        pool = multiprocessing.Pool(multiprocessing.cpu_count()*10)
        pool.map(self, [i for i in range(0, 250, 25)])

    def __call__(self, start):
        return self.get_content_by_regex(start)

if __name__ == '__main__':
    spider = Spider()
    spider.go()
    print(spider.result)
