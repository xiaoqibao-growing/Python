# coding=utf-8
"""
    进程间基本的通信，遇到的问题：
    在共享字符串的时候，在主进程中的初始化决定了这个字符串的长度，
    创建后字符串的长度固定不变，相当于把这个字符串所在的地址复制给一个指针，
    并且在字符串的首地址记录了自身的长度，
    在以后读取这个值的时候就会去读取那一段固定长度的内容，而不管现在的新内容长度是多少，
    举个例子：比如我们在主进程初始化一段字符串 "abcde",一旦初始化，长度就固定了，
    现在长度是5，然后我们在其他进程赋值，我们尝试赋值为"abcdefg",此时执行会报错，
    因为长度超标了，我们在赋值为 "yes"，
    最后输出结果为 "yes&efg"(此处的&是代表一个不可显示的字符，不同的环境下显示不同，
    有可能显示空格，有可能显示null)。也就是说长短都不行，必须和初始化字符串等长。
    于是得出这样一个结论，如果你要共享一个字符串，
    那么在子进程中赋值时必须赋值长度相当的字符串。
    建议在子进程中可以先检查字符串长度，然后在根据需要拼接指定长度的字符串。
"""
import multiprocessing


def worker(num, mystr, arr):
    num.value *= 2
    mystr.value = "ok"

    for i in range(len(arr)):
        arr[i] = arr[i]*(-1) + 1.5

def dump_vars(num, mystr, arr):
    print("num: %d" % num.value)
    print("str: %s" % mystr[:])
    print("arr: %s" % arr[:])


if __name__ == '__main__':
    nums = multiprocessing.Value('i', 5)
    mystr = multiprocessing.Array('c', "just for test")
    arr = multiprocessing.Array('d', [1.0, 1.5, -2.0])

    dir(mystr)
    print("init value")
    dump_vars(nums, mystr, arr)

    ps = [multiprocessing.Process(target=worker, args=(nums, mystr, arr)) for x in range(3)]
    for p in ps:
        p.start()

    for p in ps:
        p.join()

    print("after all finished")
    dump_vars(nums, mystr, arr)
