# Complete the function that accepts a string parameter,
# and reverses each word in the string. All spaces in 
# the string should be retained.

def reverse_words(text):
    result = ''
    word = ''
    for i in text:
        if i == ' ':
            result += word[::-1]
            word = ''
            result += i
        else:
            word += i
    return result + word[::-1]

assert reverse_words("This is an example!") == "sihT si na !elpmaxe"
assert reverse_words("double  spaces") == "elbuod  secaps"
