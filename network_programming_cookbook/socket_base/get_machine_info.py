#-*- coding=utf-8 -*-
import socket
from binascii import hexlify


def get_local_machine_info():
	"""
	获取本机的名字和IP地址
	"""
	host_name = socket.gethostname()
	host_ip = socket.gethostbyname(host_name)

	return host_name, host_ip


def get_remote_machine_info(remote_host):
	"""
	获取远程服务器的IP
	"""
	try:
		remote_host_ = socket.gethostbyname(remote_host)
	except Exception as e:
		print(e)
	else:
		return remote_host_

	return None


def convert_ipv4_address(ipv4):
	"""
	将IPV4转换为32为打包的字符
	"""
	ipv4_ = socket.inet_aton(ipv4)

	return hexlify(ipv4_)  # 以16进制保存二进制数据


def get_service_name(port, protocal):
	"""
	通过网络协议和端口找到服务名
	"""
	return socket.getservbyport(port, protocal)


def convert_data(data):
	"""
	socket可以将网络数据转化为本地的16或者32为字节序，
	也可以将机器发出去的数据转为16或者32位的网络序列
	"""
	data_ntohl = socket.ntohl(data)
	data_htonl = socket.htonl(data)

	return data_ntohl, data_htonl


def get_socket_timeout():
	"""
	获取socket的超时时间。
	"""
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.settimeout(100)

	return s.gettimeout()


if __name__ == '__main__':
	info = get_socket_timeout()

	print(info)
