#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-10 11:28:38
# @Author  : xuejun (xuemyjun@gmail.com)


def recursively_sum(values: list, i: int) -> int:
    """递归求列表的和"""

    # 基线条件
    if len(values[i:]) == 0:
        return 0

    # 递归条件
    return values[i] + recursively_sum(values, i + 1)


def recursively_sum_1(values: list) -> int:
    """递归求列表的和"""
    if values == []:
        return 0

    return values[0] + recursively_sum_1(values[1:])


def recursively_length(values: list, i: int) -> int:
    """递归求列表元素个数"""
    if len(values[i:]) == 0:
        return 1

    return 1 + recursively_length(values[i:], i + 1)


def recursively_length_1(values: list) -> int:
    """递归求元素个数"""
    if values == []:
        return 0

    return 1 + recursively_length_1(values[1:])


def recursively_get_max(values: list, i: int) -> int:
    """递归求出列表中的最大值"""
    if len(values) == 1:
        return values[0]

    return values[i] if values[i] > recursively_get_max(values[i + 1:], i)\
        else recursively_get_max(values[i + 1:], i)


def recursively_get_max_1(values: list) -> int:
    if len(values) == 1:
        return values[0]

    return values[0] if values[0] > recursively_get_max_1(values[1:])\
        else recursively_get_max_1(values[1:])


if __name__ == '__main__':
    print(recursively_sum([1, 3, 4], 0))
    print(recursively_sum_1([1, 3, 4]))
    print(recursively_length([1, 3, 4], 0))
    print(recursively_length_1([1, 3, 4]))
    print(recursively_get_max([1, 3, 4], 0))
    print(recursively_get_max_1([1, 3, 4]))
