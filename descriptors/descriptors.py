#-*- coding=utf-8 -*-

class RevealAccess(object):
	def __get__(self, obj, objtype):
		print("self in RevealAccess:{}".format(self))
		print("self:{}\nobjtype:{}".format(self, obj, objtype))


class MyClass(object):
	x = RevealAccess()

	def test(self):
		print("self in MyClass:{}".format(self))


if __name__ == '__main__':
	m = MyClass()
	m.test()

	print(MyClass().__name__)

	m.x
	MyClass.x
