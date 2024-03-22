def count_bits(n):
    return str(bin(n)).lstrip('0b').count('1')


print(count_bits(5))
