def approx_equals(array_a, array_b):
    return sum(((num[0] - num[1]) ** 2) for num in zip(array_a, array_b)) / len(array_a)


a1 = [1, 2, 3]
a2 = [4, 5, 6]

assert approx_equals(a1, a2) == 9

b1 = [10, 20, 10, 2]
b2 = [10, 25, 5, -2]
assert approx_equals(b1, b2) == 16.5

c1 = [0, -1]
c2 = [-1, 0]
assert approx_equals(c1, c2) == 1

d1 = [10, 10]
d2 = [10, 10]
assert approx_equals(d1, d2) == 0
