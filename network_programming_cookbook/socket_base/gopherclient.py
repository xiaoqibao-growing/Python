# -*- coding=utf-8 -*-

import socket
import sys


class Connection(object):
    """
    A socket connection object.
    """
    __slots__ = ['host', 'port', 'timeout']

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def get_socket(self):
        try:
            socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as se:
            print("Create socket error:%s" % se)
            sys.exit(1)
        else:
            return socket_

    def connect(self, socket_):
        try:
            socket_.connect((self.host, self.port))
        except socket.gaierror as sg:
            print("Error host or port:%s" % sg)
            sys.exit(1)
        except socket.error as se:
            print("Error connecting error:%s" % se)
            sys.exit(1)

    def makefile(self, filename, socket_):
        fd = s.makefile('wr', 0)
        fd.write(filename + "\r\n")

        for line in fd.readlines():
            sys.stdout.write(line)

    def receive(self, socket_):
        buf = socket_.recv(2048)
        if not len(buf):
            return
        print(buf)

    def send(self, socket_):
        while True:
            self.receive(socket_)

            content = raw_input("Please input something:\nYou can input # to terminate.>")

            if content != "#":
                socket_.sendall(content)
            else:
                break

    def close(self, socket_):
        try:
            socket_.close()
        except socket.error as se:
            print("Error when close socket:%s" % se)


if __name__ == '__main__':
    connection = Connection("localhost", 51432)
    s = connection.get_socket()
    connection.connect(s)
    # connection.receive(s)
    connection.send(s)
    # connection.close(s)
