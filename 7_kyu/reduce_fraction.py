def reduce_fraction(fraction):
    for i in range(min(fraction), 0, -1):
        if min(fraction) % i == 0 and max(fraction) % i == 0:
            a, b = fraction
            return a // i, b // i


print(reduce_fraction((45, 120)))
# example: [45, 120] --> [3, 8]
