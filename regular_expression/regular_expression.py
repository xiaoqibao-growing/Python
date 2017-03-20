#-*- coding=utf-8 -*-
import re


"""
向re.compile()传入一个字符串值，将返回一个Regex对象；
Regex对象的search()方法来查找传入的字符串，如果匹配成功，则返回一个Match对象；
匹配失败则返回None。Match对象有一个group方法能用来查找匹配的结果。
当然，Regex对象有一个findall()方法，可以找到所有匹配的字符。
"""
regex = re.compile(".")  # 匹配一个任意字符，不包含换行符。
result = regex.search("abcdefg")
print(result.group())  # 返回a

regex = re.compile("^a")  # 匹配以a开头的字符
result = regex.search("abcdefg")
print(result.group())  # 返回a

regex = re.compile("g$")  # 匹配以a开头的字符
result = regex.search("abcdefg")
print(result.group())  # 返回g

regex = re.compile(".*")  # 匹配一个任意字符0次或者多次。
result = regex.search("abcdefg")
print(result.group())  # 返回abcdefg

regex = re.compile(".+")  # 匹配一个任意字符1次或者多次。
result = regex.search("abcdefg")
print(result.group())  # 返回abcdefg

regex = re.compile("^a(b)?.*")  # ?前的字符出现或不出现都匹配，如果多个字符就用括号括起来，不括起来就表示问好前所有的字符。
result = regex.search("acdefg")
print(result.group())  # 返回acdefg

regex = re.compile(".*?")  # 以非贪婪的形式匹配，匹配尽可能少的数据。
result = regex.search("abcdefg")
print(result.group())  # 返回""，匹配尽可能少的数据，则为0次。

regex = re.compile(".+?")  # 以非贪婪的形式匹配，匹配尽可能少的数据。
result = regex.search("abcdefg")
print(result.group())  # 返回a，匹配尽可能少的数据，则为1次。

regex = re.compile(".{3}")  # 匹配前面的数据m次，{m}。
result = regex.search("abcdefg")
print(result.group())  # 返回abc，匹配3次，则为三个字母，abc。

regex = re.compile(".{3,5}")  # 匹配前面的数据m次到n此，{m,n}。
result = regex.search("abcdefg")
print(result.group())  # 返回abcde，匹配5此。

regex = re.compile(".{3,5}?")  # 匹配前面的数据m次到n此，{m,n}，加上?号，则会以最少的匹配，匹配三次。
result = regex.search("abcdefg")
print(result.group())  # 返回abc，匹配3此。

regex = re.compile(".*\..*")  # 通过转义字符匹配.。
result = regex.search("abc.defg")
print(result.group())  # 返回abc.defg

regex = re.compile("[abcdefg]*")  # 通过[]匹配[]中指定的字符，不加*则只匹配a。
result = regex.search("abcdefg")
print(result.group())  # 返回abcdefg

regex = re.compile("abc|defg")  # 通过|匹配|两边中的一个。
result = regex.search("abcdefg")
print(result.group())  # 返回abc

regex = re.compile("ab(.*)e(.+)")  # 添加括号进行分组。
result = regex.search("abcdefg")
print(result.group(1))  # 返回abcdefg，其中group(0)中为cd, group(1)中为fg。

regex = re.compile("(?P<name>.+)efg")  # 分组，除了原有的编号外再指定一个额外的别名，这里为name。
result = regex.search("abcdefg")
print(result.group('name'))  # 返回abcd

regex = re.compile("(?P<name>.+)efg(?P=name)")  # 这里(?P=name)相当于引用了前面的分组。
result = regex.search("abcdefgabcde")
print(result.group())  # 返回abcdefgabcd，这里name的值为abcd，所以后面接abcd便可以找到。

regex = re.compile("abc(?#content)defg")  # (?#...)忽略掉...所表示的内容。
result = regex.search("abcdefga")
print(result.group())  # 返回abcdefg

regex = re.compile("abc(?=defg)")  # (?=...)先行断言，如果字符串后面的内容是=后面的内容，则匹配=前面的内容。
result = regex.search("abcdefga")
print(result.group())  # 返回abc

regex = re.compile("abc(?!defgh)")  # (?=...)负先行断言，如果字符串后面的内容不是=后面的内容，则匹配=前面的内容。
result = regex.search("abcdefga")
print(result.group())  # 返回abc

regex = re.compile("(?<=abc)defg")  # <=之后的字符串内容需要匹配表达式才能成功匹配。
result = regex.search("abcdefg")
print(result.group())  # 返回defg

regex = re.compile("(?!abc)defg")  # <=之后的字符串内容不匹配表达式才能成功匹配。
result = regex.search("123defg")
print(result.group())  # 返回defg

regex = re.compile("(.)bc(?(1).*|\d)")  # 如果具有给定id或名称的组存在，则尝试与yes-pattern匹配，如果不存在，则尝试与no-pattern匹配。
result = regex.search("abcdefg")
print(result.group())  # 返回abcdefg，因为第一组成功匹配到a

regex = re.compile("(?P<name>.*)bc(?(name).*|\d)")  # 如果具有给定id或名称的组存在，则尝试与yes-pattern匹配，如果不存在，则尝试与no-pattern匹配。
result = regex.search("abcdefg")
print(result.group())  # 返回abcdefg，因为别名name成功匹配到a

regex = re.compile("(?i)abcdefg")  # (?i)忽略大小写。
result = regex.search("AbcdeFg")
print("(?i)", result.group())  # 返回AbcddeFg

regex = re.compile(r'Agent \w+')
result = regex.sub('CENSORD', 'Agent Alice gave the secret documents to Agent Bob.')  # 使用sub方法替换匹配的字符串
print(result)

"""
可以使用多行注释的方法写复杂的正则表达式
"""
phone_regex = re.compile(r'''(
		(\d{3}|\(\d{3}\))?  # area code
		(\s|-|\.)?  # separator
		\d{3}  # first 3 digits
		(\s|-|\.)  # separator
		\d{4}
		(\s*(ext|x|ext.)\s*\d{2, 5})?  # extension
	)''', re.VERBOSE)  # 第二个参数还可以是re.IGNOREECASE(忽略大小写), re.DOTALL(所有字符包括换行)