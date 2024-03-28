def longest_consec(strarr, k):
    if len(strarr) < k or not strarr or k < 1:
        return ''
    start = 0
    end = k
    max_str = ''
    while end <= len(strarr):
        curr = ''.join(strarr[start:end])
        if len(curr) > len(max_str):
            max_str = curr
        start += 1
        end += 1
    return max_str


print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))  # "abigailtheta"
print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3))  # "ixoyx3452zzzzzzzzzzzz"
print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], -3))  # ""
