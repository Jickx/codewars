def valid_braces(string):
    brackets = {'(': ')', '{': '}', '[': ']'}
    result = []
    for s in string:
        if s in brackets.keys():
            result.append(s)
        elif result:
            if s == brackets[result[-1]]:
                result.pop()
    return True if not result else False


print(valid_braces("(){}[]"))  # True
print(valid_braces("([{}])"))  # True
print(valid_braces("(}"))  # False
print(valid_braces("[(])"))  # False
print(valid_braces("[({})](]"))  # False
print(valid_braces("())({}}{()][]["))  # False
