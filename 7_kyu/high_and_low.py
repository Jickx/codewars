# In this little assignment you are given a string of space separated
# numbers, and have to return the highest and lowest number.

def high_and_low(numbers):
    numbers_list = numbers.split()
    max, min = int(numbers_list[0]), int(numbers_list[0])
    for i in numbers_list:
        if int(i) > max:
            max = int(i)
    for i in numbers_list:
        if int(i) < min:
            min = int(i)
    return str(max) + ' ' + str(min)


assert high_and_low("1 2 3 4 5") == "5 1"
assert high_and_low("1 2 -3 4 5") == "5 -3"
assert high_and_low("1 9 3 4 -5") == "9 -5"
