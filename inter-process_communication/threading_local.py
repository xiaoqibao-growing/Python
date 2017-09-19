# coding=utf-8
"""
    在threading module中，有一个非常特别的类local。一旦在主线程实例化了一个local，
    它会一直活在主线程中，
    并且又主线程启动的子线程调用这个local实例时，它的值将会保存在相应的子线程的字典中。

    如果想在当前线程保存一个全局值，并且各自线程互不干扰，使用local类吧。
"""
from threading import Thread, local, enumerate, currentThread

local_data = local()
local_data.name = 'local_data'


class TestThread(Thread):
    def run(self):
        print(currentThread())
        print(local_data.__dict__)
        local_data.name = self.getName()
        local_data.add_by_sub_thread = self.getName()
        print(local_data.__dict__)


if __name__ == '__main__':
    print(currentThread())
    print(local_data.__dict__)

    t1 = TestThread()
    t1.start()
    t1.join()

    t2 = TestThread()
    t2.start()
    t2.join()

    print(currentThread())
    print(local_data.__dict__)
