#-*- coding=utf-8 -*-

"""
	简单工厂模式：创建型设计模式，关注于类的简单创建。
		模式特点：工厂根据条件产生不同功能的类。
"""

class Operation(object):
	def get_result(self):
		pass


class OperationAdd(Operation):
	def get_result(self):
		return self.op1 + self.op2


class OperationSub(Operation):
	def get_result(self):
		return self.op1 - self.op2


class OperationMul(Operation):
	def get_result(self):
		return self.op1 * self.op2


class OperationDiv(Operation):
	def get_result(self):
		try:
			result = self.op1/self.op2
			return result
		except ValueError as ve:
			print("Error:%s." % ve)
			return


class OperationUndef(Operation):
	def get_result(self):
		print("Undefine operation.")
		return 0


class OperationFactory(object):
	operation = {}
	operation['+'] = OperationAdd()
	operation['-'] = OperationSub()
	operation['*'] = OperationMul()
	operation['/'] = OperationDiv()

	def create_operation(self, ch):
		if ch in self.operation:
			op = self.operation[ch]
		else:
			op = OperationUndef()

		return op


if __name__ == '__main__':
	op = raw_input("operator:")
	opa = raw_input("a:")
	opb = raw_input("b:")

	factory = OperationFactory()
	cal = factory.create_operation(op)
	cal.op1 = opa
	cal.op2 = opb

	print(cal.get_result())
