def expanded_form(num):
    if num < 10:
        return f'{num}'
    remainder = int(str(num)[1:])
    num -= remainder
    return f'{num}' if remainder == 0 else f'{num} + ' + expanded_form(remainder)


print(expanded_form(70304))  # '70000 + 300 + 4'
print(expanded_form(9000000))  # '9000000'
