def find_outlier(integers):
    odd = []
    even = []
    for i in integers:
        odd.append(i) if i % 2 != 0 else even.append(i)
    return odd.pop() if len(odd) == 1 else even.pop()


print(find_outlier([2, 4, 6, 8, 10, 3]))  # 3
