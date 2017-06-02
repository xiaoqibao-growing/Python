# coding=utf-8

'''
问题：你有一个线程队列集合，想为到来的元素轮询它们，
就跟你为一个客户端请求去轮询一个网络连接集合的方式一样。

解决方案：对于轮询问题的一个常见解决方案中有个很少有人知道的技巧，
包含了一个隐藏的回路网络连接。
本质上讲其思想就是：对于每个你想要轮询的队列，你创建一对连接的套接字。
然后你在其中一个套接字上面编写代码来标识存在的数据，
另外一个套接字被传给 select() 或类似的一个轮询数据到达的函数。
'''

import socket
import os
import threading
import select

from Queue import Queue


class PollableQueue():
    def __init__(self):
        self.queue = Queue(20)
        # Create a pair of connected sockets.
        if os.name == "posix":
            self._putsocket, self._getsocket = socket.socketpair()
        else:
            # Compatibility on non-POSIX systems
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(('127.0.0.1', 0))
            server.listen(1)

            self._putsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._putsocket.connect(server.getsockname())
            self._getsocket, _ = server.accept()
            server.close()

    def fileno(self):
        return self._getsocket.fileno()

    def put(self, item):
        self.queue.put(item)
        self._putsocket.send(b'x')

    def get(self):
        self._getsocket.recv(1)
        return self.queue.get()


def consumer(queues):
    '''
    Consumer that reads data on multiple queues simultanenously
    '''
    while True:
        can_read, _, _ = select.select(queues, [], [])
        for r in can_read:
            item = r.get()
            print('GOT:', item)


q1 = PollableQueue()
q2 = PollableQueue()
q3 = PollableQueue()
t = threading.Thread(target=consumer, args=([q1, q2, q3],))
t.setDaemon(True)
t.start()

q1.put(1)
q2.put(10)
q3.put('hello')
q2.put(15)