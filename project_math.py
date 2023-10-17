def add(*numbers):
    res = 0
    for n in numbers:
        res += n


def mult(*numbers):
    res = 1
    for n in numbers:
        res *= n
    return res
