# -*- coding:utf-8 -*-
# __author__ = xuejun
import string, urllib2


def baidu_tieba(url, begin_page, end_page):
    for i in range(begin_page, end_page):
        sName = string.zfill(i, 5) + '.html'
        print("正在下载第" + str(i) + "个网页")
        with open(sName, "wb") as sn:
            response = urllib2.urlopen(url + str(i))
            sn.write(response.read())


if __name__ == '__main__':
    baidu_tieba('http://tieba.baidu.com/f?kw=骑士&ie=utf-8&pn=', 1,3)