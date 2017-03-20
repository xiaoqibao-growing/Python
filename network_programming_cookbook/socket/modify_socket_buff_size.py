#-*- coding=utf-8 -*-
import socket


SEND_BUF_SIZE = 4096
REVEIVE_BUF_SIZE = 4096

def modify_buff_size():
	"""
	修改socket接收缓冲和发送缓冲的大小。
	"""
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Get the size of the socket's send buffer.
	bufsize = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
	print("Buffer size [Before]:%d") % bufsize

	s.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
	s.setsockopt(
		socket.SOL_SOCKET,
		socket.SO_SNDBUF,
		SEND_BUF_SIZE
		)  # 修改发送缓冲。
	s.setsockopt(
		socket.SOL_SOCKET,
		socket.SO_RCVBUF,
		REVEIVE_BUF_SIZE
		)  # 修改接收缓冲。

	bufsize = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)  # 获取当前发送缓冲区大小。

	print("Buffer size [Before]:%d") % bufsize


if __name__ == '__main__':
	modify_buff_size()
