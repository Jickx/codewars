# def is_valid_walk(walk):
#     # determine if walk is valid
#     ctr_y, ctr_x = 0, 0
#     for i in walk:
#         if i == "w":
#             ctr_y += 1
#         elif i == 'e':
#             ctr_y -= 1
#         elif i == 'n':
#             ctr_x += 1
#         elif i == 's':
#             ctr_x -= 1
#     return ctr_x == ctr_y == 0 and len(walk) == 10

def is_valid_walk(walk):
    return (len(walk) == 10
            and walk.count('n') == walk.count('s')
            and walk.count('e') == walk.count('w'))


assert is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']) is True
assert is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']) is False
assert is_valid_walk(['w']) is False
assert is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']) is False
