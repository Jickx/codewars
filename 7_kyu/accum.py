def accum(st):
    return '-'.join((c * (i + 1)).title() for i, c in enumerate(st))


assert accum("abcd") == "A-Bb-Ccc-Dddd"
assert accum("RqaEzty") == "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
assert accum("cwAt") == "C-Ww-Aaa-Tttt"
