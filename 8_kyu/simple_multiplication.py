# Multiplying a given number by eight if it is an even number
# and by nine otherwise.

def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9


assert simple_multiplication(1) == 9
assert simple_multiplication(8) == 64
assert simple_multiplication(4) == 32
assert simple_multiplication(5) == 45
