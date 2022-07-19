# Write an algorithm that takes an array and moves all of the zeros to the
# end, preserving the order of the other elements.

def move_zeros(lst: list[int]) -> list[int]:
    result = [i for i in lst if i != 0]
    return result + [0] * (len(lst) - len(result))


assert move_zeros([
    1, 0, 1, 2, 0, 1, 3]) == [1, 1, 2, 1, 3, 0, 0]
assert move_zeros([
    1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [
    1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
assert move_zeros([
    9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9
]) == [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
