def sumsquares(lst):
    result = 0
    for i in lst:
        if isinstance(i, int):
            result += i ** 2
        else:
            result += sumsquares(i)
    return result
