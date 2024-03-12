def set_reducer(inp):
    result = []
    i = 0
    while i < len(inp):
        ctr = 1
        while i + 1 < len(inp) and inp[i] == inp[i + 1]:
            ctr += 1
            i += 1
        result.append(ctr if ctr > 1 else 1)
        i += 1
    if len(result) == 1:
        return result[0]
    return set_reducer(result)


print(set_reducer([8, 1, 6, 1, 2, 7, 7, 7, 7, 6, 5, 3, 2, 1, 8]))
