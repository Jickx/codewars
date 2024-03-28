def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num - 1):
        if num % i == 0:
            return False
    return True


print(is_prime(2))  # true
print(is_prime(73))  # true
print(is_prime(1))  # false
print(is_prime(-1))  # false
