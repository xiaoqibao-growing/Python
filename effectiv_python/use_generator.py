# -*- coding:utf-8 -*-
# __author__ = xuejun

"""
    zh:我们应该考虑用生成器来改写直接返回列表的函数
    en:We should consider using the generator to override the function that returns the list directly.
"""


def index_words(text):
    result = []

    if text:
        result.append(0)

    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)

    return result


def index_words_iter(text):
    if text:
        yield 0

    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

address = 'Four score and seven years ago...'
results = index_words_iter(address)
print list(results)