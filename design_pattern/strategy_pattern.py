#-*- coding:utf-8 -*-

"""
	策略模式：定义一系列算法，把每一个算法封装起来，并且使它们可以相互替换。
	本模式可以使得算法可独立于使用它的客户而变化。
	适用性：
		1）许多相关的类仅仅是行为有异。 “策略”提供了一种用多个行为中的一个行为来配置一个类的方法。
		   即一个系统需要动态地在几种算法中选择一种。
		2）需要使用一个算法的不同变体。例如，你可能会定义一些反映不同的空间 /时间权衡的算法。
		   当这些变体实现为一个算法的类层次时 ,可以使用策略模式。
		3）算法使用客户不应该知道的数据。可使用策略模式以避免暴露复杂的、与算法相关的数据结构。
		4）一个类定义了多种行为 , 并且这些行为在这个类的操作中以多个条件语句的形式出现。
		   将相关的条件分支移入它们各自的Strategy类中以代替这些条件语句。
"""

class CashSuper(object):
	def accept_cash(self, money):
		return 0


class CashNormal(CashSuper):
	def accept_cash(self, money):
		return money


class CashRebate(CashSuper):
	discount = 0

	def __init__(self, ds):
		self.discount = ds

	def accept_cash(self, money):
		return money*self.discount


class CashReturn(CashSuper):
	total, ret = 0, 0

	def __init__(self, t, r):
		self.total = t
		self.ret = r

	def accept_cash(self, money):
		if money > self.total:
			return money - self.ret
		else:
			return money


class CashContext(object):
	def __init__(self, csuper):
		self.cs = csuper

	def get_result(self, money):
		return self.cs.accept_cash(money)


if __name__ == '__main__':
	money = raw_input("moeny:")

	strategy = {}
	strategy[1] = CashContext(CashNormal())
	strategy[2] = CashContext(CashRebate(0.8))
	strategy[3] = CashContext(CashReturn(300, 100))

	ctype = raw_input("type:[1] for normal;[2] for 80% discount;[3] for 300 -100")

	if ctype in strategy:
		cc = strategy(ctype)
	else:
		print("Undefine type. User normal mode.")
		cc = strategy(1)

	print("You will pay: %d" % cc.get_result(moeny))
