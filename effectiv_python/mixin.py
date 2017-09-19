#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-04 14:07:10
# @Author  : xuejun (xj174850@163.com)
# @Link    : https://github.com/NeuObito
# @Version : 0.1

import os


class ToDicMixin(object):
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        output = {}

        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)

        return output

    def _traverse(self, key, value):
        if isinstance(value, ToDicMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value


class BinaryTree(ToDicMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


if __name__ == '__main__':
    tree = BinaryTree(
        10,
        left=BinaryTree(7, right=BinaryTree(9)),
        right=BinaryTree(13, left=BinaryTree(11))
    )
    print(tree.__dict__)
    print(tree.to_dict())
