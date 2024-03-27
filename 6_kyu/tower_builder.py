def tower_builder(n_floor):
    result = []
    width = (n_floor * 2) - 1
    for x in range(1, 2 * n_floor, 2):
        stars = x * '*'
        line = stars.center(width)
        result.append(line)
    return result


# print(tower_builder(3))  # ['  *  ', ' *** ', '*****']
# print(tower_builder(2))
print(tower_builder(4))
