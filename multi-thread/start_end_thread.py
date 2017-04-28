# coding=utf-8
"""
由于全局解释锁（GIL）的原因，Python 的线程被限制到同一时刻只允许一个线程执行这样一个执行模型。
所以，Python 的线程更适用于处理I/O和其他需要并发执行的阻塞操作（比如等待I/O、等待从数据库获取数据等等），
而不是需要多处理器并行的计算密集型任务。
"""

import time
from threading import Thread


def countdown(n):
    while n > 0:
        print("T-minus:", n)
        n -= 1
        time.sleep(1)


class CountDown(object):
    """
     除了如上所示的两个操作，并没有太多可以对线程做的事情。
     你无法结束一个线程，无法给它发送信号，无法调整它的调度，也无法执行其他高级操作。
     如果需要这些特性，你需要自己添加。
     比如说，如果你需要终止线程，那么这个线程必须通过编程在某个特定点轮询来退出。
    """
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print("T-minus:", n)
            n -= 1
            time.sleep(2)


if __name__ == '__main__':
    t = Thread(target=countdown, args=(10,))
    """ Daemon线程会被粗鲁的直接结束，它所使用的资源（已打开文件、数据库事务等）
     无法被合理的释放。因此如果需要线程被优雅的结束，请设置为非Daemon线程，
     并使用合理的信号方法，如事件Event。"""
    t.setDaemon(True)
    t.start()

    if t.is_alive():
        print("Still running.")
    else:
        print("Completed.")

    t.join()

    c = CountDown()
    t = Thread(target=c.run, args=(10,))
    t.start()
    time.sleep(5)
    c.terminate()
    t.join()
