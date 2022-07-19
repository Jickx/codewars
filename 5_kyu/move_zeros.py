# Write an algorithm that takes an array and moves all of the zeros to the
# end, preserving the order of the other elements.

def move_zeros(lst: list[int]) -> list[int]:
    result = []
    i = 0
    ctr = 0
    while i < len(lst):
        if lst[i] == 0:
            ctr += 1
            i += 1
            continue
        else:
            result.append(lst[i])
            i += 1
    result.extend([0 for i in range(ctr)])
    return result


assert move_zeros([1, 0, 1, 2, 0, 1, 3]) == [1, 1, 2, 1, 3, 0, 0]
assert move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [
    1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
assert move_zeros([
    9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9
]) == [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
