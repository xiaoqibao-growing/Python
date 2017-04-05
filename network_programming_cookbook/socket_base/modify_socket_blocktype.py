#-*- coding=utf-8 -*-
import socket


def modify_socket_blocktype():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# s.setblocking(1)  # 1为阻塞模式
	s.setblocking(0)  # 0为非阻塞模式
	s.settimeout(0.1)
	s.bind(("127.0.0.1", 0))

	socket_address = s.getsockname()
	print("Trival Server launched on socket: %s" % str(socket_address))

	while True:
		s.listen(1)


if __name__ == '__main__':
	modify_socket_blocktype()
