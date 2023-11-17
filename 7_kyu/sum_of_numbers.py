def get_sum(a, b):
    seq = []
    x = min(a, b)
    y = max(a, b)
    for i in range(x, y + 1):
        seq.append(i)
    return sum(seq)


print(get_sum(0, -1))
