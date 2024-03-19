def sum_nested(lst):
    result = []

    for i in lst:
        if isinstance(i, int):
            result.append(i)
        else:
            result.append(sum_nested(i))
    return sum(result)
