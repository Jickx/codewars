# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

def dig_pow(n, p):
    map_n = list(map(int, [x for x in str(n)]))
    result = []
    for i in range(len(map_n)):
        result.append(map_n[i] ** (i + p))
    return sum(result) // n if sum(result) % n == 0 else -1


print(dig_pow(695, 2))  # 2
print(dig_pow(46288, 3))  # 51
