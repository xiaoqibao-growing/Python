#-*- coding=utf-8 -*-

"""
	装饰器模式：动态地为对象增加额外的职责；允许向一个现有的对象添加新的功能，同时不改变其结构。
	这种类型的设计模式属于结构型设计模式，它是作为现有类的一个包装。
"""

class Person(object):
	def __init__(self, tname):
		self.name = tname

	def show(self):
		print("Dressed %s" % self.name)


class Finery(Person):
	component = None

	def __init__(self):
		pass

	def decorate(self, ct):
		self.component = ct

	def show(self):
		if not self.component:
			self.component.show()


class TShirts(Finery):
	def __init__(self):
		pass

	def show():
		print("Big Trouser")
		self.component.show()


class BigTrouser(Finery):
	def __init__(self):
		pass

	def show(self):
		print("Big Trouser")
		self.component.show()


if __name__ == '__main__':
	p = Person("somebody")
	bt = BigTrouser()
	ts = TShirts()
	bt.decorate(p)
	ts.decorate(bt)
	ts.show()
