def comp(array1, array2):
    if array1 is None or array2 is None or len(array1) != len(array2):
        return False
    array1.sort(key=abs)
    array2.sort(key=abs)

    return all(i ** 2 == j for i, j in list(zip(array1, array2)))


a1 = [11, 19, 19, 19, 121, 144, 144, 161, 1008]
a2 = [121, 361, 361, 14641, 20736, 20736, 25921, 36100]
print(comp(a1, a2))  # True

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 11, 121 * 121, 144 * 144, 190 * 190, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
print(comp(a1, a2))  # False

a1 = [-14, 0, 1, 19, 144, 161, 191, 195]
a2 = [0, 1, 196, 361, 20736, 25921, 36481, 38025]

print(comp(a1, a2))  # False
