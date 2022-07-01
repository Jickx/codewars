# Create a function that takes a list of non-negative integers and strings and
# returns a new list with the strings filtered out.

def filter_list(l):
    return [i for i in l if not isinstance(i, str)]

assert filter_list([1,2,'a','b']) == [1,2]
assert filter_list([1,'a','b',0,15]) == [1,0,15]
assert filter_list([1,2,'aasf','1','123',123]) == [1,2,123]