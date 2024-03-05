import string


def rot13(message):
    alphabet = {c: i for i, c in enumerate(string.ascii_lowercase)}
    res = ''
    for i in message:
        if i.isalpha():
            new_index = int((alphabet[i.lower()] + 13) % 26)
            if i.lower() == i:
                res += string.ascii_lowercase[new_index]
            else:
                res += string.ascii_uppercase[new_index]
        else:
            res += i
    return res


print(rot13('test'))
print(rot13('Test'))
print(rot13('aA bB zZ 1234 *!?%'))

# ('test'), 'grfg',
# ('Test'), 'Grfg',
# ('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%'
