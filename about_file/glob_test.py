# -*- coding=utf-8 -*-
import glob

"""
glob.glob(pathname) pathname可以是相对路径也可以是绝对路径，返回与路径名匹配的可能为空的路径名列表，路径名必须是包含路径规范的字符串。
"""
file_list = glob.glob("*")  # 获取当前文件夹下的所有文件
print(file_list)

file_list = glob.glob("g*")  # 获取当前文件夹下所有以g开头的文件
print(file_list)

file_list = glob.glob("*.py")  # 获取当前文件夹下所有以.py结尾的文件
print(file_list)

"""
glob.iglob(pathname) 同glob.glob()，iglob()返回的是一个生成器。
"""
file_list = glob.iglob("*")  # 获取当前文件夹下的所有文件
print(file_list)  # 这里file_list是一个生成器。
