def wave(s):
    result = []
    if s:
        for i in range(len(s) - 1):
            if s[i].isalpha():
                result.append(s.lower()[:i] + s.upper()[i] + s.lower()[i + 1:])
        if s[-1].isalpha():
            result.append(s.lower()[:-1] + s.upper()[-1])
    return result


print(wave(' code wars '))
print(wave(''))
