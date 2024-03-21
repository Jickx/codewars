def set_reducer(inp):
    if len(set(inp)) == 1:
        return len(inp)
    else:
        prev = 0
        cur = 1
        while cur < len(inp):
            if inp[prev] == inp[cur]:
                while inp[prev] == inp[cur] and cur < len(inp) - 1:
                    cur += 1
                inp = inp[:prev] + [cur - prev] + inp[cur:]
                cur = prev + 2
                prev = cur - 1
            else:
                inp[prev] = 1
                cur += 1
                prev += 1
            if prev == len(inp) - 1:
                inp[prev] = 1
    return set_reducer(inp)


print(set_reducer([0, 4, 6, 8, 8, 8, 5, 5, 7]))  # 111321 3111 13 11 2
print(set_reducer([8, 1, 6, 1, 2, 7, 7, 7, 7, 6, 5, 3, 2, 1, 8]))  # 111113111111 516111 3
