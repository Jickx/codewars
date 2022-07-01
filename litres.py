# Nathan loves cycling.
# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres
# of water per hour of cycling.
# You get given the time in hours and you need to return the number of litres
# Nathan will drink, rounded to the smallest value.

def litres(time):
    return time // 2

assert(litres(3)) == 1
assert(litres(6.7)) == 3
assert(litres(11.8)) == 5