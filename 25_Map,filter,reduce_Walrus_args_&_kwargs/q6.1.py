# use map() to convert [1, 2, 3, 4, 5] into cubes

num = [1, 2, 3, 4, 5]
squared = map(lambda x: x**3, num)
print(list(squared)) 