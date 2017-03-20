# -*- coding:utf-8 -*-
# __author__ = xuejun
from multiprocessing import Pool
import random


def compute(n):
    return sum(
        [random.randint(1, 100) for i in range(1000000)]
    )


if __name__ == '__main__':
    pool = Pool(8)
    results = pool.map(compute, range(8))
    print(results)
