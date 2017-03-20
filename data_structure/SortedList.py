# -*- coding:utf-8 -*-
# __author__ = xuejun
"""
创建一个一直保持有序的列表。
"""

import bisect


class SortedList(list):
    def __init__(self, iterable):
        super(SortedList, self).__init__(sorted(iterable))

    def insort(self, item):
        print(self)
        bisect.insort(self, item)

    def index(self, value, start=None, stop=None):
        place = bisect.bisect_left(self[start:stop], value)
        if start:
            place += start

        end = stop or len(self)
        if place < end and self[place] == value:
            return place

        raise ValueError("%s is not in list" % value)


if __name__ == '__main__':
    sl = SortedList([2, 4, 1, 3])
    sl.insort(5)

    print(sl)
