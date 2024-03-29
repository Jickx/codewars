def sum_dig_pow(a, b):
    result = []
    for num in range(a, b + 1):
        dig_pow = 0
        for i in range(len(str(num))):
            dig_pow += int(str(num)[i]) ** (i + 1)
        if dig_pow == num:
            result.append(dig_pow)
    return result


print(sum_dig_pow(1, 10))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum_dig_pow(1, 100))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
