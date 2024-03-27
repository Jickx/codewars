def is_pangram(s):
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if c not in s.lower():
            return False
    return True


print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
print(is_pangram("1bcdefghijklmnopqrstuvwxyz"))
print(is_pangram("ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"))
