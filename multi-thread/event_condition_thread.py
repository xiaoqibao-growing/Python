# coding=utf-8

"""
    如果程序中的其他线程需要通过判断某个线程的状态来确定自己下一步的操作，这时线程同步问题就会变得非常棘手。
    为了解决这些问题，我们需要使用 threading 库中的 Event 对象。
    Event 对象包含一个可由线程设置的信号标志，它允许线程等待某些事件的发生。
    在初始情况下，event 对象中的信号标志被设置为假。
    如果有线程等待一个 event 对象，而这个 event 对象的标志为假，
    那么这个线程将会被一直阻塞直至该标志为真。
    一个线程如果将一个 event 对象的信号标志设置为真，它将唤醒所有等待这个 event 对象的线程。
    如果一个线程等待一个已经被设置为真的 event 对象，那么它将忽略这个事件，继续执行。
    下边的代码展示了如何使用 Event 来协调线程的启动：
"""

import time

from threading import Thread, Event


def countdown(n, started_evt):
    """
        event 对象最好单次使用，就是说，
        你创建一个 event 对象，让某个线程等待这个对象，一旦这个对象被设置为真，
        你就应该丢弃它。尽管可以通过 clear() 方法来重置 event 对象，
        但是很难确保安全地清理 event 对象并对它重新赋值。
        很可能会发生错过事件、死锁或者其他问题（特别是，你无法保证重置
        event 对象的代码会在线程再次等待这个 event 对象之前执行）。
    """
    print("countdown starting.")
    started_evt.set()

    while n > 0:
        print("T-minus:", n)
        n -= 1
        time.sleep(2)


def use_event():
    # Create the event object that will be used to signal startup
    started_evt = Event()

    # Launch the thread and pass the startup event
    print("Launching countdown.")
    t = Thread(target=countdown, args=(10, started_evt))
    t.start()

    # Wait for the thread to start
    started_evt.wait()
    print("countdown is running.")

"""
event对象的一个重要特点是当它被设置为真时会唤醒所有等待它的线程。
如果你只想唤醒单个线程，最好是使用信号量或者 Condition 对象来替代。
"""
class PeriodTimer(object):
    """
        如果一个线程需要不停地重复使用 event 对象，你最好使用 Condition 对象来代替。
        下面的代码使用 Condition 对象实现了一个周期定时器，每当定时器超时的时候，
        其他线程都可以监测到：
    """
    def __init__(self, interval):
        import threading
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        t = Thread(target=self.run)
        t.setDaemon(True)

        t.start()

    def run(self):
        """
            Run the timer and notify waiting threads after each interval.
        """
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^= 1
                # notify（）方法唤醒等待条件变量的线程之一，
                # 如果有的话等待。 notifyAll（）方法唤醒所有等待条件变量的线程。
                self._cv.notify_all()

    def wait_for_tick(self):
        """
            Wait for the next tick of the timer.
        """
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                # wait（）方法释放锁，然后阻塞，直到它被另一个线程中的相同条件变量的notify（）
                # 或notifyAll（）调用唤醒为止）。一旦唤醒，它重新获得锁并返回。
                # 也可以指定超时。
                self._cv.wait()

ptimer = PeriodTimer(5)
ptimer.start()

def countdown_condtion(nticks):
    while nticks > 0:
        ptimer.wait_for_tick()
        print("T-minus:", nticks)
        nticks -= 1

def countup_condition(last):
    n = 0
    while n < last:
        ptimer.wait_for_tick()
        print("Counting:", n)
        n += 1

Thread(target=countdown_condtion, args=(10,)).start()
Thread(target=countup_condition, args=(5,)).start()
