def approx_equals(array_a, array_b):
    return sum(((num[0] - num[1]) ** 2) for num in zip(array_a, array_b)) / len(array_a)
