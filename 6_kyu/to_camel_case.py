import re


def to_camel_case(text):
    if not text:
        return ''
    else:
        return text[0].lower() + ''.join(map(str.title, re.split("[_|-]", text)))[1:] if text[0].islower() else ''.join(
            map(str.title, re.split("[_|-]", text)))


print(to_camel_case("The_stealth-warrior"))
print(to_camel_case("the_stealth_warrior"))
