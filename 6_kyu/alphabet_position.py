import string


def alphabet_position(text):
    alphabet = {c: i + 1 for i, c in enumerate(string.ascii_lowercase)}
    return ' '.join([str(alphabet[i]) for i in text.lower() if i.isalpha()])


assert (alphabet_position("The sunset sets at twelve o' clock.") ==
        "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
