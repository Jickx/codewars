def permutations(string):
    result = []
    string_list = list(string)

    if len(string_list) == 1:
        return [string]

    for i in range(len(string_list)):
        n = string_list.pop(0)
        perms = permutations(string_list)

        for perm in perms:
            result.append(n + ''.join(perm))

        string_list.append(n)

    return set(result)
