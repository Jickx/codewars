# from math import sqrt
#
#
# def find_next_square(sq):
#     # Return the next square if sq is a square, -1 otherwise
#     if sq >= 0:
#         res = sqrt(sq)
#         if res % 1 == 0:
#             return int(pow(res + 1, 2))
#     return -1

def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (int(root) + 1) ** 2
    return -1


assert find_next_square(121) == 144
