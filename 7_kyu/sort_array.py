# You will be given an array of numbers. You have to sort the odd 
# numbers in ascending order while leaving the even numbers at 
# their original positions.

def sort_array(lst):
    result = [None] * len(lst)
    odds = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            result[i] = lst[i]   
        else:
            odds.append(lst[i])
    sorted_odds = sorted(odds)
    sorted_odds.reverse()
    for i in range(len(result)):
        if result[i] == None:
            result[i] = sorted_odds.pop()
    return result


assert sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
assert sort_array([5, 3, 1, 8, 0]) == [1, 3, 5, 8, 0]
assert sort_array([]) == []
assert sort_array([11, 1, 2, 8, 3, 4, 5]) == [1, 3, 2, 8, 5, 4, 11]