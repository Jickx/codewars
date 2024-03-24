def tribonacci(signature, n):
    if n < 3:
        return signature[:n]
    return tribonacci(signature + [sum(signature[-3:])], n) if len(signature) < n else signature


print(tribonacci([1, 1, 1], 10))  # [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
print(tribonacci([1, 1, 1], 1))
