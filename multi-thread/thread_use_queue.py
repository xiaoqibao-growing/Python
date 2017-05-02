# coding=utf-8
__author = "xuejun"

"""
    1、Queue 对象已经包含了必要的锁，所以你可以通过它在多个线程间多安全地共享数据。
    当使用队列时，协调生产者和消费者的关闭问题可能会有一些麻烦。
    一个通用的解决方法是在队列中放置一个特殊的值，当消费者读到这个值的时候，终止执行。

    2、使用队列来进行线程间通信是一个单向、不确定的过程。
    通常情况下，你没有办法知道接收数据的线程是什么时候接收到的数据并开始工作的。
    不过队列对象提供一些基本完成的特性，比如下边这个例子中的 task_done() 和 join() ：
"""
from Queue import Queue
from threading import Thread

# Object that signals shutdown
_sentinel = object()

# A thread that produces data
def producer(out_q):
    while True:
        # Produce some data
        out_q.put(data)

    # Put the sentinel on the queue to indicate completion
    out_q.put(_sentinel)  # 1


# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()

        if data is _sentinel:
            '''
                消费者在读到这个特殊值之后立即又把它放回到队列中，将之传递下去。
                这样，所有监听这个队列的消费者线程就可以全部关闭了。
            '''
            in_q.put(_sentinel)
            break

        # Indicate completion 2
        in_q.task_done()


# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))

t1.start()
t2.start()

q.join()

'''
尽管队列是最常见的线程间通信机制，但是仍然可以自己通过创建自己的数据结构并添加所需的锁和同步机制来实现线程间通信。
最常见的方法是使用 Condition 变量来包装你的数据结构。下边这个例子演示了如何创建一个线程安全的优先级队列
'''
import heapq
import threading


class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._count = 0
        self._cv = threading.Condition()

    def put(self, item, priority):
        with self._cv:
            heapq.heappush(self._queue, (-priority, self._count, item))
            self._count += 1
            self._cv.notify()

    def get(self):
        with self._cv:
            while len(self._queue) == 0:
                self._cv.wait()

            return heapq.heappop(self._queue)[-1]


'''
如果一个线程需要在一个“消费者”线程处理完特定的数据项时立即得到通知，
你可以把要发送的数据和一个 Event 放到一起使用，这样“生产者”就可以通过这个Event对象来监测处理的过程了。
'''
from threading import Event


# A thread that produces data
def producer_event(out_q):
    while running:
        # Make an (data, event) pair and hand it to the consumes
        evt = Event()
        out_q.put((data, evt))

        # Wait for the consumer to process the item
        evt.wait()


# A thread that consumes data
def consumer_event(in_q):
    while True:
        # Get some data
        data, evt = in_q.get()

        evt.set()
