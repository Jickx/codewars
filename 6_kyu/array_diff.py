def array_diff(a, b):
    return [i for i in a if i not in b]


print(array_diff([1, 2], [1]))  # [2]
