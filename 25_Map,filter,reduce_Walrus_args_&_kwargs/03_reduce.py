# The reduce() function applies a function of two arguments cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a single value.reduce is not a built-in function; it must be imported from the module.

from functools import reduce
num = [1, 2, 3, 4, 5, 6]
#     [3, 3, 4, 5, 6]
#     [6, 4, 5, 6]
#     [10, 5, 6]
#     [15, 6]
#     [21]

def sum(a,b):
    return a + b

c = reduce(sum, num)
print(c)