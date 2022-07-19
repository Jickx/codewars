# Given two arrays of strings a1 and a2 return a sorted array r in
# lexicographical order of the strings of a1 which are substrings
# of strings of a2.


def in_array(array1, array2):
    result = set()
    array1 = set(array1)
    array2 = set(array2)
    for i in array1:
        for j in array2:
            if i in j:
                result.add(i)
    return sorted(list(result))


assert in_array(
    ["live", "arp", "strong"],
    ["lively", "alive", "harp", "sharp", "armstrong"]
) == ['arp', 'live', 'strong']

assert in_array(
    ["arp", "mice", "bull"],
    ["lively", "alive", "harp", "sharp", "armstrong"]
) == ['arp']
