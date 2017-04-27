# coding=utf-8
import multiprocessing


class Test(object):
    def __init__(self):
        pass

    def f(self, x):
        return x*x

    def go(self):
        pool = multiprocessing.Pool(4)
        print(pool.map(self, range(10)))

    def __call__(self, x):
        return self.f(x)


if __name__ == '__main__':
    test = Test()
    test.go()  # 这里为什么会出问题
