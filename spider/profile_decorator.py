# -*- coding:utf-8 -*-
# __author__ = xuejun
import cProfile
import pstats
import os


def do_cprofile(filename):
    """
    Decorator for function profiling.
    :param filename:
    :return:
    """
    def wrapper(func):
        def profiled_func(*args, **kwargs):
            profile = cProfile.Profile()
            profile.enable()
            result = func(*args, **kwargs)
            profile.disable()

            sortby = "tottime"
            ps = pstats.Stats(profile).sort_stats(sortby)
            ps.dump_stats(filename)

        return profiled_func

    return wrapper
