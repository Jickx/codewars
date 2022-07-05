# You will be given an array of numbers. You have to sort the odd 
# numbers in ascending order while leaving the even numbers at 
# their original positions.

def sort_array(lst):
    odds = sorted((i for i in lst if i % 2 != 0), reverse = True)
    return [i if i % 2 == 0 else odds.pop() for i in lst]

assert sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
assert sort_array([5, 3, 1, 8, 0]) == [1, 3, 5, 8, 0]
assert sort_array([]) == []
assert sort_array([11, 1, 2, 8, 3, 4, 5]) == [1, 3, 2, 8, 5, 4, 11]