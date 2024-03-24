def unique_in_order(sequence):
    if not sequence:
        return []
    result = [sequence[0]]
    for i in sequence:
        if i != result[-1]:
            result.append(i)
    return result


print(unique_in_order([1, 2, 2, 3, 3]))  # [1, 2, 3]
print(unique_in_order('AAAABBBCCDAABBB'))  # ['A', 'B', 'C', 'D', 'A', 'B']
