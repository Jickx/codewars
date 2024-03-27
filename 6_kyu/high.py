import string


def high(text):
    abc = {c: i+1 for i, c in enumerate(string.ascii_lowercase)}
    text_dct = {w: sum([abc[c] for c in w]) for w in text.split()}
    max_num = text_dct[max(text_dct, key=lambda x: text_dct[x])]
    return next(iter([x for x in text.split() if text_dct[x] == max_num]))


print(high('man i need a taxi up to ubud'))  # 'taxi'
print(high('what time are we climbing up the volcano'))  # 'volcano'
print(high('aa b'))  # 'aa'
