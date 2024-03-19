# 0 grains need 0 cells
# 1 grain needs 1 cell
# 2 grains need 2 cells
# 3 grains need 2 cells
# 4 grains need 3 cells


def squares_needed(grains):
    i = 0
    prev = 0
    curr = 1
    while True:
        if prev <= grains < curr:
            return i
        else:
            i += 1
            prev = curr
            curr += curr


print(squares_needed(4))
print(squares_needed(349793859))
