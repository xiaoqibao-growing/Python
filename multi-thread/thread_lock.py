# coding=utf-8
__author__ = "xuejun"

'''
    你需要对多线程程序中的临界区加锁以避免竞争条件。
'''

from threading import Lock, RLock, Semaphore


class SharedCount(object):
    '''
    线程调度本质上是不确定的，因此，在多线程程序中错误地使用锁机制可能会导致
    随机数据损坏或者其他的异常行为，我们称之为竞争条件。
    为了避免竞争条件，最好只在临界区（对临界资源进行操作的那部分代码）使用锁。
    '''
    def __init__(self, initial_count=0):
        self._count = initial_count
        self._count_lock = Lock()

    def incre(self, delta=1):
        '''
        Lock 对象和 with 语句块一起使用可以保证互斥执行，
        就是每次只有一个线程可以执行 with 语句包含的代码块。
        with 语句会在这个代码块执行前自动获取锁，在执行结束后自动释放锁。
        '''
        with self._count_lock:
            self._count += delta

        # 老的方法
        # self._count_lock.acquire()
        # self._count += delta
        # self._count_lock.release()

    def decre(self, delta):
        with self._count_lock:
            self._count -= delta


'''
一个 RLock （可重入锁）可以被同一个线程多次获取，
主要用来实现基于监测对象模式的锁定和同步。
在使用这种锁的情况下，当锁被持有时，只有一个线程可以使用完整的函数或者类中的方法。
'''
class SharedCountRLock(object):
    _lock = RLock()
    def __init__(self, initial_count):
        self._count = initial_count

    def incre(self, delta=1):
        with SharedCount._lock:
            self._count += delta

    def decre(self, delta=1):
        with SharedCount._lock:
            self._count -= delta


'''
相对于简单地作为锁使用，信号量更适用于那些需要在线程之间引入信号或者限制的程序。
比如，你需要限制一段代码的并发访问量
'''
class SharedCountSemaphore(object):
    import urllib.request
    _semaphore = Semaphore(5)

    def fetch_url(url):
        with SharedCountSemaphore._semaphore:
            return urllib.request.urlopen(url)
