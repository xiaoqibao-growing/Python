# coding=utf-8
__author = "xuejun"

"""
    Queue 对象已经包含了必要的锁，所以你可以通过它在多个线程间多安全地共享数据。
    当使用队列时，协调生产者和消费者的关闭问题可能会有一些麻烦。
    一个通用的解决方法是在队列中放置一个特殊的值，当消费者读到这个值的时候，终止执行
"""
from Queue import Queue
from threading import Thread

# 
# A thread that produces data
def producer(out_q):
    while True:
        # Produce some data
        out_q.put(data)


# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()


# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))

t1.start()
t2.start()
