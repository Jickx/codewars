# Write an algorithm that takes an array and moves all of the zeros to the
# end, preserving the order of the other elements.

def move_zeros(lst: list[int]) -> list[int]:
    result = [i for i in lst if i != 0]
    return result + [0] * (len(lst) - len(result))
