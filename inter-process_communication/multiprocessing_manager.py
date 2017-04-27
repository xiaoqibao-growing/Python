# coding=utf-8
"""
    Python中进程间共享数据，除了基本的queue，pipe和value+array外，
    还提供了更高层次的封装。使用multiprocessing.Manager可以简单地使用这些高级接口。
    Manager()返回的manager对象控制了一个server进程，
    此进程包含的python对象可以被其他的进程通过proxies来访问。
    从而达到多进程间数据通信且安全。
    Manager支持的类型有list,dict,Namespace,Lock,RLock,Semaphore,BoundedSemaphore,
    Condition,Event,Queue,Value和Array。
"""
import time
import multiprocessing

def worker(d, key, value):
    d[key] = value


if __name__ == '__main__':
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    mpr = multiprocessing.Manager()
    d = mpr.dict()
    jobs = [multiprocessing.Process(target=worker, args=(d, i, i*2))
        for i in range(10)]

    for i in jobs:
        i.start()

    for i in jobs:
        i.join()

    print("Results:")
    for key in dict(d):
        print(key, d[key])
