# coding=utf-8
"""
    在不同程序间如果有同时对同一个队列操作的时候，为了避免错误，
    可以在某个函数操作队列的时候给它加把锁，
    这样在同一个时间内则只能有一个子进程对队列进行操作。
"""
from multiprocessing import Process, Queue, Pool
import multiprocessing
import os, time, random

def write(q, lock):
    # 写数据进程执行的代码
    lock.acquire()  # 加上锁
    for value in ["A", "B", "C"]:
        print("Put %s to queue..." % value)
        q.put(value)
    lock.release()  # 释放锁

def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print('Get %s from queue.' % value)
            time.sleep(random.random())
        else:
            break


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    queue = Queue()
    lock = manager.Lock()
    pw = Process(target=write, args=(queue, lock))
    pr = Process(target=read, args=(queue,))

    pw.start()
    pr.start()

    pw.join()
