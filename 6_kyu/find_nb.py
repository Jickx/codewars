def find_nb(m):
    result = 1
    sum_vol = 0
    while sum_vol <= m:
        sum_vol += result ** 3
        if sum_vol == m:
            return result
        result += 1
    return -1


print(find_nb(1071225))  # 45
