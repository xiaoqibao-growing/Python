#-*- coding=utf-8 -*-
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())  
"""soup对html进行处理后输出，soup对象将html转化为一个复杂的树形结构，
每个节点都是一个Python对象，所有对象可以归纳为四种：
Tag、NavigableString、BeautifulSoup以及Comment
"""

print(soup.title)  # 通过标签名称获取一个Tag
print(soup.title.name)  # 通过标签的name属性获取属性名称
print(soup.title.string)  # 通过标签的string属性获取标签内容

print(soup.a)  # 如果有多个标签的话，只匹配找到的第一个标签

print(soup.p['class'])  # 通过标签中的网页属性获取内容

print(soup.find_all('p'))  # 通过find_all()获取所有的相关标签
print(soup.find(id="link3"))  #在soup对象中通过字符串寻找标签

for link  in soup.find_all("a"):  # 获取所有的a标签
	print(link['class'])  # 从a标签中获取href内容

print(soup.get_text())  #从文档中获取所有内容，即除去页面标签和标签的相关属性之外的内容
