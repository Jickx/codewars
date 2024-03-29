# def two_sum(numbers, target):
#     for i in range(len(numbers)):
#         for j in range(len(numbers)):
#             if numbers[i] + numbers[j] == target and i != j:
#                 return i, j

def two_sum(numbers, target):
    num_dct = {}
    for i, n in enumerate(numbers):
        remainder = target - n
        if n in num_dct:
            return num_dct[n], i
        num_dct[remainder] = i


print(two_sum([1, 2, 3], 4))  # returns (0, 2) or (2, 0)
print(two_sum([3, 2, 4], 6))  # returns (1, 2) or (2, 1)
