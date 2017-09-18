#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-18 15:55:48
# @Author  : xuejun (xuemyjun@gmail.com)
# @Link    : https://github.com/Nabitor
# @Version : 0.1

from functools import partial, wraps

import logging


def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)

    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    """
    Add logging to a function, level is the logging
    level, name is the logger name, and message is
    the log message. If name and message aren't sepecified,
    they default to function's module and name.
    """
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(new_level):
            nonlocal level
            print(new_level)
            level = new_level

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            print(newmsg)
            logmsg = newmsg

        return wrapper

    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print("Spam")


if __name__ == '__main__':
    add(2, 3)
    add.set_message("nihao")
