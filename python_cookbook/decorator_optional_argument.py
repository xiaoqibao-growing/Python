#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-18 17:11:18
# @Author  : xuejun (xuemyjun@gmail.com)
# @Link    : https://github.com/Nabitor
# @Version : 0.1

import logging

from functools import wraps, partial


def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)

    return wrapper


@logged
def add(x, y):
    return x + y


@logged(level=logging.CRITICAL, name="example")
def spam():
    print("spam")


if __name__ == '__main__':
    add(2, 3)
