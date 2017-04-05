#-*- coding=utf-8
import sys
import socket
import argparse


def main():
	"""
	argparse模块使得编写友好的命令行参数变的简单。
	"""
	parser = argparse.ArgumentParser(description="Socket Error Example.")
	parser.add_argument("--host", action="store", dest="host", required=False)
	parser.add_argument("--port", action="store", dest="port", type=int, required=False)
	parser.add_argument("--file", action="store", dest="file", required=False)

	given_args = parser.parse_args()
	host, port, filename = given_args.host, given_args.port, given_args.file
	print(host, port)

	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket创建失败时抛出错误。
	except socket.error as e:
		print("Socket creating error: %s" % e)
		sys.exit(1)

	try:
		s.connect((host, port))  # socket不能正常连接时,如果是地址错误，抛出gaierror；不能连接抛出error。
	except socket.gaierror as ge:
		print("Address-related error connecting to server: %s" % ge)
		sys.exit(1)
	except socket.error as e:
		print("Connecting error: %s" % e)
		sys.exit(1)

	try:
		s.sendall("GET %s HTTP/1.0\r\n\r\n" % filename)  # 发送数据失败时抛出错误。
	except socket.error as e:
		print("Error sending data: %s" % e)


	while 1:
		try:
			buf = s.recv(2048)
		except socket.error as e:  # 接收数据失败时抛出错误。
			print("Error receiving data: %s" % e)
			sys.exit(1)

		if not len(buf):
			break

		sys.stdout.write(buf)

if __name__ == '__main__':
	main()
