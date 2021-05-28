# return a new list with the strings filtered out
def filter_list(l):
    list2 = []
    for i in l:
        if isinstance(i, str) == True:
            continue
        else:
            list2.append(i)

    return (list2)