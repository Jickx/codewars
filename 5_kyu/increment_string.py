def increment_string(s):
    if s == '' or s[-1].isalpha():
        return s + '1'
    i = len(s) - 1
    while i >= 0:
        if s[i].isdigit():
            i -= 1
        else:
            break
    return s[:i + 1] + str(int(s[i + 1:]) + 1).zfill(len(s) - i - 1)
