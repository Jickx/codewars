# 0 grains need 0 cells
# 1 grain needs 1 cell
# 2 grains need 2 cells
# 3 grains need 2 cells
# 4 grains need 3 cells


def squares_needed(grains):
    if grains < 1:
        return 0
    return 1 + squares_needed(grains // 2)


print(squares_needed(4))
print(squares_needed(349793859))
