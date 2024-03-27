def split_strings(str):
    if len(str) % 2 != 0:
        str += '_'
    print(str)
    return [str[i] + str[i + 1] for i in range(0, len(str), 2)]


print(split_strings("asdfadsfs"))  # ['as', 'df', 'ad', 'sf']
