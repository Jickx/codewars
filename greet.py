# Make a function that will return a greeting statement that uses an input;
# your program should return, "Hello, <name> how are you doing today?".
# [Make sure you type the exact thing I wrote or the program may not execute properly]

def greet(name):
    return f"Hello, {name} how are you doing today?"

assert greet('Ryan') == "Hello, Ryan how are you doing today?"
assert greet('Shingles') == "Hello, Shingles how are you doing today?"