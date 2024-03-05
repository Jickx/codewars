from functools import reduce


def number(bus_stops):
    # Good Luck!
    return sum(on - off for on, off in bus_stops)


assert number([[10, 0], [3, 5], [5, 8]]) == 5
assert number([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]) == 21
assert number([[0, 0]]) == 0
