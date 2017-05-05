# coding=utf-8

'''
要实现发布/订阅的消息通信模式，你通常要引入一个单独的“交换机”或“网关”对象作为所有消息的中介。
也就是说，不直接将消息从一个任务发送到另一个，而是将其发送给交换机，
然后由交换机将它发送给一个或多个被关联任务。
一个交换机就是一个普通对象，负责维护一个活跃的订阅者集合，并为绑定、解绑和发送消息提供相应的方法。
'''

from collections import defaultdict
from contextlib import contextmanager


class Exchange(object):
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)

    '''
    某种意义上，这个和使用文件、锁和类似对象很像。通常很容易会忘记最后的 detach() 步骤。
    为了简化这个，你可以考虑使用上下文管理器协议。
    '''
    @contextmanager
    def subscribe(self, *tasks):
        for task in tasks:
            self.attach(task)

        try:
            yield
        finally:
            for task in tasks:
                self.detach(task)


_exchanges = defaultdict(Exchange)

# Return the Exchange instance associated with a given name
def get_exchange(name):
    return _exchanges[name]


# Example of a task. Any object with a send() method.
class Task(object):
    def send(self):
        pass


task_a = Task()
task_b = Task()

# Example of getting an Exchange.
exc = get_exchange('name')
with exc.subscribe(task_a, task_b):
    exc.send("msg1")
    exc.send("msg2")

# exc.attach(task_a)
# exc.attach(task_b)
#
# exc.send('msg1')
# exc.send('msg2')
#
# exc.detach(task_a)
# exc.detach(task_b)

'''
尽管对于这个问题有很多的变种，不过万变不离其宗。
消息会被发送给一个交换机，然后交换机会将它们发送给被绑定的订阅者。
'''
