# coding=utf-8
__author__ = "xuejun"

'''
有时在多线程编程中，你需要只保存当前运行线程的状态。
要这么做，可使用 thread.local() 创建一个本地线程存储对象。
对这个对象的属性的保存和读取操作都只会对执行线程可见，而其他线程并不可见。
'''

from socket import socket, AF_INET, SOCK_STREAM

import threading

class LazyConnection(object):
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.local = threading.local()

    def __enter__(self):
        if hasattr(self.local, 'sock'):
            raise RuntimeError("Already connected.")

        self.local.sock = socket(self.family, self.type)
        self.local.sock.connect(self.address)
        return self.local.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.local.sock.close()
        del self.local.sock

def test(conn):
    with conn as sock:
        sock.send(b'Get /index.html HTTP/1.0\r\n')
        sock.send(b'Host: www.python.org\r\n')

        sock.send(b'\r\n')

        from functools import partial
        resp = b''.join(iter(partial(sock.recv, 8192), b''))

    print("Got {} bytes".format(len(resp)))

if __name__ == '__main__':
    conn = LazyConnection(('www.python.org', 80))

    t1 = threading.Thread(target=test, args=(conn,))
    t2 = threading.Thread(target=test, args=(conn,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
