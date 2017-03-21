# -*- coding:utf-8 -*-
# __author__ = xuejun


def consumer():
    status = True
    while True:
        n = yield status
        print("我拿到了{}".format(n))

        if n == 3:
            status = False


def producer(consumer):
    n = 5
    while n > 0:
        yield consumer.send(n)
        n -= 1


if __name__ == '__main__':
    c = consumer()
    c.send(None)
    p = producer(c)
    for status in p:
        if not status:
            print("我只要3,4,5就醒啦。")
            break

        print("程序结束")

