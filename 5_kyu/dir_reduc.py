def dir_reduc(arr, is_valid=False):
    if len(arr) == 1 or is_valid:
        return arr
    i = 0
    while i + 1 < len(arr):
        if (arr[i] == "NORTH" and arr[i + 1] == "SOUTH") or (arr[i] == "SOUTH" and arr[i + 1] == "NORTH"):
            arr = arr[:i] + arr[i + 2:]
            i = max(0, i)
        if (arr[i] == "EAST" and arr[i + 1] == "WEST") or (arr[i] == "WEST" and arr[i + 1] == "EAST"):
            arr = arr[:i] + arr[i + 2:]
            i = max(0, i)
        else:
            is_valid = True
    return dir_reduc(arr, is_valid)


print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST", "WEST"]))  # ['WEST']
