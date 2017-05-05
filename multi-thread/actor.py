# coding=utf-8

__author__ = "xuejun"

'''
actore模式是一种最古老的也是最简单的并行和分布式计算解决方案。
事实上，它天生的简单性是它如此受欢迎的重要原因之一。
简单来讲，一个actor就是一个并发执行的任务，只是简单的执行发送给它的消息任务。
响应这些消息时，它可能还会给其他actor发送更进一步的消息。actor之间的通信是单向和异步的。
因此，消息发送者不知道消息是什么时候被发送，也不会接收到一个消息已被处理的回应或通知。
'''

from Queue import Queue
from threading import Thread, Event


# Sentinel used for shutdown
class ActorExit(Exception):
    pass


class Actor(object):
    def __init__(self):
        self._maibox = Queue()

    def send(self, msg):
        '''
        Send a message to the actor.
        '''
        self._maibox.put(msg)

    def recv(self):
        '''
        Receive an incoming message.
        '''
        msg = self._maibox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg

    def close(self):
        '''
        Close the actor, thus shutting it down.
        '''
        self.send(ActorExit)

    def start(self):
        '''
        Start concurrent execution.
        '''
        self._terminated = Event()
        t = Thread(target=self._bootstarp)

        t.daemon = True
        t.start()

    def _bootstarp(self):
        try:
            self.run()
        except ActorExit as e:
            pass
        finally:
            self._terminated.set()

    def join(self):
        self._terminated.wait()

    def run(self):
        '''
        Run method to be implemented by the user.
        '''
        while True:
            msg = self.recv()


class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print("Got:", msg)


def print_actor():
    while True:
        try:
            msg = yield
            print("Got:", msg)
        except GeneratorExit as ge:
            print("Actor terminating.")


p = print_actor()
# p.start()
next(p)
p.send("Hello")
p.send("World")
p.close()
# p.join()
