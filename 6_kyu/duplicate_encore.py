def duplicate_encode(word):
    return ''.join(['(' if word.count(x) == 1 else ')' for x in word])


print(duplicate_encode("din"))  # "((("
