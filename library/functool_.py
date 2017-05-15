# coding=utf-8

'''
functools 是 Python 中很简单但也很重要的模块，主要是一些 Python 高阶函数相关的函数。
'''

from functools import partial, partialmethod, wraps
from functools import update_wrapper, cmp_to_key, total_ordering


def add(x, y):
    return x + y

add_y = partial(add, 4)
print(add_y(4))


class Cell(object):
    def __init__(self):
        self._alive = False

    @property
    def alive(self):
        return self._alive

    def set_state(self, state):
        self._alive = bool(state)

    set_alive = partialmethod(set_state, True)
    set_dead = partialmethod(set_state, False)


c = Cell()
print(c.alive)

c.set_alive()
print(c.alive)

# 装饰器相关
'''
说到“接受函数为参数，以函数为返回值”，在 Python 中最常用的当属装饰器了。
functools 库中装饰器相关的函数是 update_wrapper、wraps，
还搭配 WRAPPER_ASSIGNMENTS 和 WRAPPER_UPDATES 两个常量使用，
作用就是消除 Python 装饰器的一些负面作用。
'''

def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper

@decorator
def add(x, y):
    return x + y

print(add.__name__)  # print wrapper

'''
可以看到被装饰的函数的名称，也就是函数的 __name__ 属性变成了 wrapper，
这就是装饰器带来的副作用，
实际上add 函数整个变成了 decorator(add)，而 wraps 装饰器能消除这些副作用。
'''

def decorator_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def decorator_update_wrapper(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return update_wrapper(wrapper, func)


# @decorator_wraps
@decorator_update_wrapper
def add_wraps(x, y):
    return x + y

print(add_wraps.__name__)  # print add_wraps


# cmp_to_key, total_ordering
'''
cmp_to_key 是 Python 2.7 中新增的函数，用于将比较函数转换为 key 函数，
这样就可以应用在接受 key 函数为参数的函数中，比如 sorted、max 等等。

total_ordering 同样是 Python 2.7 中新增函数，用于简化比较函数的写法。
如果你已经定义了 __eq__ 方法，
以及 __lt__、__le__、__gt__ 或者 __ge__() 其中之一， 即可自动生成其它比较方法。
'''

print(sorted(range(5), key=cmp_to_key(lambda x, y: y-x)))


@total_ordering
class Student(object):
    def __eq__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) == \
            (other.lastname.lower(), other.firstname.lower()))

    def __lt__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) < \
            (other.lastname.lower(), other.firstname.lower()))

print(dir(Student))
