def reverse(n):
    def inner(n, r):
        if n == 0:
            return r
        else:
            return inner(n // 10, r * 10 + n % 10)

    return inner(n, r=0)


print(reverse(1234))  # 4321
print(reverse(10987))  # 78901
print(reverse(1020))  # 201
