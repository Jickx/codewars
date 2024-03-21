def deep_count(a, ctr=0):
    for i in a:
        ctr += 1
        if isinstance(i, list):
            ctr = deep_count(i, ctr)
    return ctr
