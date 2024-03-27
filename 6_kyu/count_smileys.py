import re


def count_smileys(arr):
    return len(list(filter(lambda x: re.match(r'[;:][-~]?[)D]', x), arr)))


print(count_smileys([':D', ':~)', ';~D', ':)']))  # 4
