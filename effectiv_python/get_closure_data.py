# -*- coding:utf-8 -*-
# __author__ = xuejun

"""
    This program will tell you how to get data from closure.
"""


def sort_priority(values, group):
    def helper(x):
        if x in group:
            return 0, x
        return 1, x

    values.sort(key=helper)


def sort_priority2(values, group):
    found = False

    def helper(x):
        if x in group:
            found = True  # seems simple, however, this is equivalent to have created a found while value is True
            return 0, x
        return 1, x

    values.sort(key=helper)
    return found


def sort_priority3(values, group):
    found = False

    def helper(x):
        # nonlocal found  # just support python 2.*
        if x in group:
            return 0, x
        return 1, x

    values.sort(key=helper)


def sort_priority4(values, group):
    found = [False]  # as you know, list can be changed.

    def helper(x):
        if x in group:
            found[0] = True
            return 0, x
        return 1, x

    values.sort(key=helper)
    return found


class Sorter(object):
    """
        We can use a class for this function.
    """
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return 0, x
        return 1, x

if __name__ == '__main__':
    numbers = [8, 3, 2, 1, 5, 4, 7, 6]
    group = {2, 3, 5, 7}

    # sort_priority(numbers, group)
    # found = sort_priority2(numbers, group) # run it, we found that the value of found is False.

    # print sort_priority4(numbers, group)

    sorter = Sorter(group)
    numbers.sort(key=sorter)
    assert sorter.found is True