def narcissistic(value):
    return sum(map(lambda x: x ** len(str(value)), [int(x) for x in str(value)])) == value


print(narcissistic(7))  # True
print(narcissistic(371))  # True
