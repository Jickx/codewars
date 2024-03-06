def increment_string(s):
    if s == '' or s[-1].isalpha():
        return s + '1'
    i = len(s) - 1
    while i >= 0:
        if s[i].isdigit():
            i -= 1
        else:
            break
    return s[:i + 1] + str(int(s[i + 1:]) + 1).zfill(len(s) - i - 1)


print(increment_string('009'))

assert increment_string("foo") == "foo1"
assert increment_string("foobar001") == "foobar002"
assert increment_string("foobar1") == "foobar2"
assert increment_string("foobar00") == "foobar01"
assert increment_string("foobar99") == "foobar100"
assert increment_string("foobar099") == "foobar100"
assert increment_string("fo99obar99") == "fo99obar100"
assert increment_string("") == "1"
