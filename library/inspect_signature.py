#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-20 12:11:18
# @Author  : xuejun (xuemyjun@gmail.com)
# @Link    : https://github.com/Nabitor
# @Version : 0.1


"""Visualizing Callable Objects' Signature"""


from inspect import signature
from functools import partial, wraps


class FooMeta(type):

    def __new__(mcls, name, bases, dct, *, bar: bool=False):
        return super().__new__(mcls, name, bases, dct)

    def __init__(cls, name, bases, dct, **kwargs):
        return super().__init__(name, bases, dct)


class Foo(metaclass=FooMeta):

    def __init__(self, spam: int=42):
        self.spam = spam

    def __call__(self, a, b, *, c) -> tuple:
        return a, b, c

    @classmethod
    def spam(cls, a):
        return a


def shared_vars(*shared_args):
    """Decorator factory that defines shared variables that are
       passed to every invocation of the function"""

    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            full_args = shared_args + args
            return f(*full_args, **kwargs)

        # Override signature
        sig = signature(f)
        sig = sig.replace(parameters=tuple(signature.parameters.values())[1:])
        wrapper.__signature__ = sig

        return wrapper
    return decorator


@shared_vars({})
def example(_state, a, b, c):
    return _state, a, b, c


def formate_signature(obj):
    print(str(signature(obj)))


if __name__ == '__main__':
    formate_signature(FooMeta)
    formate_signature(Foo)
    formate_signature(Foo().__call__)
    formate_signature(Foo.__call__)
    formate_signature(Foo.spam)
    formate_signature(partial(Foo().__call__, 1, c=3))
    formate_signature(example)
    formate_signature(partial(example, 1, 2))  # 柯里化了
    print(signature(partial(example, 1, 2)).parameters)
    formate_signature(partial(partial(example, 1, 2), c=3))
