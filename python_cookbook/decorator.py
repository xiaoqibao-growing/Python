#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-18 13:55:18
# @Author  : xuejun (xuemyjun@gmail.com)
# @Link    : https://github.com/Nabitor
# @Version : 0.1

import logging
import time

from functools import wraps


def timethis(func):
    """Decorator that reports the execution time"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def countdown(n):
    """Counts Down"""
    while n > 0:
        n -= 1


def logged(level, name=None, message=None):
    """
    Add logging to a function, level is the logging
    level, name is the logger name, and message is
    the log message. If name and message aren't specified,
    they default to the function's module and name.
    """
    def decorate(func):
        logname = name if name else func.__module
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        return wrapper


if __name__ == '__main__':
    countdown(1000000)

    # 解除装饰器，访问原始函数，如果有多个装饰器，这种行为是不可预知的
    countdown.__wrapped__(10000)
