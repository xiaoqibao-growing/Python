#-*- coding=utf-8 -*-
import chardet
import urllib2
import re

from threading import Thread


def get_content(urlpath):
	"""
	第一步：试试直接请求。
	这时如果我们直接访问，会被服务器拒绝，报502错误，且提示Server Hangup。
	遇到这种问题怎么办呢，那就只能添加请求头了。
	"""
	response = urllib2.urlopen(urlpath, timeout=15)
	content = response.read()

	return content


def get_content_by_add_headers(urlpath):
	"""
	第二步：添加请求头。
	为了能有一个直观的函数印象，所以这里我使用了很多单词的驼峰法。。
	headers哪里来的，可以通过你的浏览器通过开发者工具获得。
	"""
	headers={
		'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
					(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
	}

	request = urllib2.Request(url=urlpath, headers=headers)

	response = urllib2.urlopen(request)
	content = response.read()

	encode = chardet.detect(content)['encoding']
	if encode.lower() == 'utf-8':
		content = content.decode("utf-8", "ignore").encode("utf-8")
	else:
		content = content.decode("gb2312", "ignore").encode("utf-8")

	return content


def get_content_by_regex(content):
	"""
	第三步：通过正则表达式获取内容，因为每个页面主体构造都是一样的，所以
	通过正则表达式很容易获取到页面中的内容。
	正则表达式相关的内容请在我Python包下的regular_expression下查看。
	内容获取到了，我们要得到发帖人名称，年龄，帖子内容以及点赞数。
	re.S为点任意匹配模式，改变了.的行为。
	"""
	"""
	regex中：第一个分组(即正则中的括号)表示发帖人，
	第二个分组表示年龄，第三个表示帖子内容，第四个为点赞数。
	"""
	regex = '<div.*?\"article\s+block\s+untagged mb15\".*?' \
		'<h2>(.*?)</h2>.*?' \
		'<div.*?Icon\">(.*?)</div>.*?' \
		'<span>(.*?)</span>.*?' \
		'<i\s.*?>(.*?)</i>.*?' \
		'<i\s.*?>(.*?)</i>.*?' \
		'</a>\s</div>'  
	pattern = re.compile(regex, re.S)
	Regex = re.findall(pattern, content)
	for item in Regex:
		yield item


result = []
def get_content_by_thread(content):
	"""
	第三步：通过正则表达式获取内容，因为每个页面主体构造都是一样的，所以
	通过正则表达式很容易获取到页面中的内容。
	正则表达式相关的内容请在我Python包下的regular_expression下查看。
	内容获取到了，我们要得到发帖人名称，年龄，帖子内容以及点赞数。
	re.S为点任意匹配模式，改变了.的行为。
	"""
	"""
	regex中：第一个分组(即正则中的括号)表示发帖人，
	第二个分组表示年龄，第三个表示帖子内容，第四个为点赞数。
	"""
	regex = '<div.*?\"article\s+block\s+untagged mb15\".*?' \
		'<h2>(.*?)</h2>.*?' \
		'<div.*?Icon\">(.*?)</div>.*?' \
		'<span>(.*?)</span>.*?' \
		'<i\s.*?>(.*?)</i>.*?' \
		'<i\s.*?>(.*?)</i>.*?' \
		'</a>\s</div>'  
	pattern = re.compile(regex, re.S)
	Regex = re.findall(pattern, content)
	for item in Regex:
		result.append(item)


if __name__ == '__main__':
	# print(get_content("http://www.qiushibaike.com"))  # 提示502，被服务器拒绝。
	# print(get_content_by_add_headers("http://www.qiushibaike.com"))  # 访问成功，但是网页信息太多。
	# content = get_content_by_add_headers("http://www.qiushibaike.com/8hr/page/9/?s=4966944")
	# for item in list(get_content_by_regex(content)):
	# 	print item[0].decode("utf-8"), item[1], item[2].decode("utf-8"), item[3], item[4]

	threads = []
	for i in range(1, 11):
		t = Thread(target=get_content_by_thread(get_content_by_add_headers("http://www.qiushibaike.com/8hr/page/"+ str(i) + "/?s=4966944")), args=[])
		t.start()	
		threads.append(t)

	for t in threads:
		t.join()

	
	with open("result.txt", "w+") as f:
		for item in result:
			f.write(item[0]+ " " + item[1] + " " + item[2] + " " + item[3] + " " + item[4])
