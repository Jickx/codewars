def find_it(seq):
    set_seq = set()
    for i in seq:
        if i in set_seq:
            set_seq.remove(i)
        else:
            set_seq.add(i)
    return next(iter(set_seq))


