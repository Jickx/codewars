def find_missing_letter(chars):
    return next(chr(ord(chars[x]) + 1) for x in range(len(chars) - 1) if ord(chars[x]) + 1 != ord(chars[x + 1]))


print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))  # 'e'
print(find_missing_letter(['O', 'Q', 'R', 'S']))  # 'P'
