def duplicate_count(text):
    return len(set([x for x in text.lower() if text.lower().count(x) > 1]))


print(duplicate_count(""))  # 0
print(duplicate_count("abcde"))  # 0
print(duplicate_count("abcdeaa"))  # 1
print(duplicate_count("abcdeaB"))  # 2
print(duplicate_count("Indivisibilities"))  # 2
