# The map() function applies a given function to each item of an iterable and returns an iterator that yields the results

num = [1, 2, 3, 45, 4, 21]

def square(x):
    return x * x

new = list(map(square, num))
print(new)

#                   or

new = list(map(lambda x: x*x, num))
print(new)