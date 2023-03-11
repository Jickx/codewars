def fizz_buzz_custom(string_one='Fizz',
                     string_two='Buzz',
                     num_one=3,
                     num_two=5):
    res = []
    for i in range(1, 101):
        if i % num_one == 0 and i % num_two == 0:
            res.append(string_one + string_two)
        elif i % num_one == 0:
            res.append(string_one)
        elif i % num_two == 0:
            res.append(string_two)
        else:
            res.append(i)
    return res


print(fizz_buzz_custom())
assert fizz_buzz_custom()[15] == 16
assert fizz_buzz_custom()[44] == "FizzBuzz"
assert fizz_buzz_custom('Hey', 'There')[25] == 26
assert fizz_buzz_custom('Hey', 'There')[11] == "Hey"
assert fizz_buzz_custom("What's ", "up?", 3, 7)[80] == "What's "

