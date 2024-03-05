def multiplies(num):
    res = set()
    for i in range(num):
        if i % 3 == 0:
            res.add(i)
        elif i % 5 == 0:
            res.add(i)
    return sum(res)


assert multiplies(4) == 3
assert multiplies(6) == 8
assert multiplies(16) == 60
assert multiplies(3) == 0
assert multiplies(5) == 3
assert multiplies(15) == 45
assert multiplies(0) == 0
assert multiplies(-1) == 0
assert multiplies(10) == 23
assert multiplies(20) == 78
assert multiplies(200) == 9168
