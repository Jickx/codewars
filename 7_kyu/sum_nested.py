def sum_nested(lst):
    result = []

    for i in lst:
        if isinstance(i, int):
            result.append(i)
        else:
            result.append(sum_nested(i))
    return sum(result)


print(sum_nested([1, [2, [3, [4]]]]))  # 10
print(sum_nested([1, [1], [[1]], [[[1]]]]))  # 4
