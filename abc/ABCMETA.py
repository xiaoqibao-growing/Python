#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-28 13:21:08
# @Author  : xuejun (xj174850@163.com)
# @Link    : https://github.com/NeuObito
# @Version : 0.1

import os

from abc import ABCMeta
from abc import abstractmethod


class ABC_META(object):
    __metaclass__ = ABCMeta


ABC_META.register(tuple)

"""
虚拟子类是通过调用metaclass是 abc.ABCMeta 的抽象基类的 register 方法注册到抽象基类门下的，
可以实现抽象基类中的部分API接口，也可以根本不实现，但是issubclass(), issubinstance()进行判断时仍然返回真值。

直接继承抽象基类的子类就没有这么灵活，在metaclass是 abc.ABCMeta的抽象基类中可以声明”抽象方法“和“抽象属性”，
直接继承自抽象基类的子类虽然判断issubclass()时为真，但只有完全覆写（实现）了抽象基类中的“抽象”内容后，才能被实例化，
而通过注册的虚拟子类则不受此影响。
"""

assert issubclass(tuple, ABC_META)
assert isinstance((), ABC_META)


class Foo(object):
    def __getitem__(self, index):
        pass

    def __len__(self):
        pass

    def get_iterator(self):
        return iter(self)


class MyIterable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __iter__(self):
        while False:
            yield None

    def get_iterator(self):
        return self.__iter__()

    @classmethod
    def __subclasshook__(cls, C):
        """
        （__subclasshook__必须定义为类方法。）
        检查子类是否被认为是此ABC的子类。
        这意味着您可以进一步自定义issubclass的行为，
        而无需在要考虑ABC子类的每个类上调用register（）。
        （这个类方法是从ABC的__subclasscheck __（）方法调用的。）

        此方法应返回True，False或NotImplemented。
        如果它返回True，则该子类被认为是该ABC的子类。
        如果它返回False，则该子类不被认为是该ABC的子类，即使它通常是一个。
                如果它返回NotImplemented，子类检查将继续使用通常的机制。
        """
        if cls is MyIterable:
            if any("__iter__" in B.__dict__ for B in C.__mro__):
                return True

        return NotImplemented


MyIterable.register(Foo)
print(MyIterable.__dict__)
