def solution(s):
    return ''.join([' ' + w if w.isupper() else w for w in s])


print(solution("camelCasing"))  # "camel Casing"
print(solution("identifier"))  # "identifier"
