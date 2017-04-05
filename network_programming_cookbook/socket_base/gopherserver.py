#-*- coding=utf-8 -*-

import socket
import sys


host = ""  # 主机设置为空字符串，这样可以接受来自任意地方的连接。
port = 51432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)  # 每次只能有一个连接

print("Server is running on port %d; press Ctrl-C to terminate." % port)

while True:
    client_sock, client_addr = s.accept()

    print(client_addr)
    while True:
        """
        同该客户端保持通话。
        """
        client_sock.send("Thank you for connecting.")
        line = client_sock.recv(1024).strip()
        client_sock.send("You enter %d characters.\n" % len(line))

    client_sock.close()
