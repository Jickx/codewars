def disemvowel(string_):
    return ''.join(i for i in string_ if i.lower() not in 'aeiou')


assert disemvowel(
    "This website is for losers LOL!") == "Ths wbst s fr lsrs LL!", "This website is for losers LOL!"
assert (disemvowel(
    "No offense but,\nYour writing is among the worst I've ever read") ==
        "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd"), \
    "No offense but,\nYour writing is among the worst I've ever read"
assert disemvowel(
    "What are you, a communist?") == "Wht r y,  cmmnst?", "What are you, a communist?"
