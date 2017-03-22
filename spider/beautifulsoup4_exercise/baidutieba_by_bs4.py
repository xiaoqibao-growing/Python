# -*- coding=utf-8 -*-
import urllib2
import sys
from bs4 import BeautifulSoup

class BaiduTieba(object):
	def __init__(self, url_path):
		self.url_path = url_path

	def get_content(self):
		try:
			html = urllib2.urlopen(self.url_path)
		except HTTPError as he:
			print("出现错误，错误码为：" + str(he.code))
			sys.exit()
		except URLError as ue:
			print("出现错误，错误原因为：" + ue.reason)
			sys.exit()

		content = html.read()
		return content

	def get_tiezi_theme(self):
		content = self.get_content()
		soup = BeautifulSoup(content, 'html.parser')

		result = []
		for a in soup.find_all("a"):			
			if a.has_attr('class') and a['class'] == "j_th_tit":
				print(a)
				result.append(a)

		return result

if __name__ == '__main__':
	baidutieba = BaiduTieba("http://tieba.baidu.com/f?ie=utf-8&kw=%E9%AA%91%E5%A3%AB%E5%90%A7&fr=search&red_tag=g0952824988")
	baidutieba.get_tiezi_theme()
