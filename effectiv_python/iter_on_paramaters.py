# -*- coding:utf-8 -*-
# __author__ = xuejun

"""
    zh:在参数上面迭代要多加小心。
    en:We should be more careful if we design a function which iterate over the parameters.
"""


def normalize(numbers):
    total = sum(numbers)
    result = []

    for value in numbers:
        percent = 100 * value / total
        result.append(percent)

    return result


def normalize_copy(numbers):
    numbers = list(numbers)
    total = sum(numbers)
    result = []

    for value in numbers:
        percent = 100 * value / total
        result.append(percent)

    return result


def normalize_func(get_iter):
    total = sum(get_iter())
    result = []

    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)

    return result


class ReadVisits(object):
    """
        Of course, we can also customize the iterator.
    """
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError('Must supply a container.')

    total = sum(numbers)
    result = []

    for value in numbers:
        percent = 100 * value / total
        result.append(percent)

    return result

if __name__ == '__main__':
    # test normalize()
    # visits = [15, 35, 80]

    # test read_visits()
    visits = read_visits("my_numbers.txt")

    # percentages = normalize(visits)
    # print percentages  # The result is [].Because The iterator can only produce a round of results.But, we can copy it.

    # percentages = normalize_copy(visits)

    # If we have a loud of data, this copy function will be bad.So we can use lambda.
    # percentages = normalize_func(lambda: read_visits("my_numbers.txt"))

    # visits = ReadVisits("my_numbers.txt")
    # percentages = normalize(visits)

    visits = [15, 35, 80]
    percentages = normalize_defensive(visits)

    print percentages
