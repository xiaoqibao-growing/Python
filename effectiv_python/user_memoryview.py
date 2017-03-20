# -*- coding:utf-8 -*-
# __author__ = xuejun


def read_random():
    with open("memoryview.txt", 'rb') as source:
        content = source.read()
        content_to_write = memoryview(content)[20:]

    print(content_to_write.tolist())


if __name__ == '__main__':
    read_random()
