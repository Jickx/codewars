def delete_nth(order, max_e):
    ctr = {c: 0 for c in set(order)}
    result = []
    for x in order:
        if ctr[x] < max_e:
            ctr[x] += 1
            result.append(x)
    return result


print(delete_nth([1, 2, 3, 1, 2, 1, 2, 3], 2))  # [1,2,3,1,2,3]
