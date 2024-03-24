from functools import reduce


def persistence(n):
    return 0 if n < 10 else persistence(reduce(lambda x, y: x * y, [int(x) for x in map(int, str(n))])) + 1


print(persistence(39))  # 3
