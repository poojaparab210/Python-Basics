# Use filter() to get only even numbers from [10, 11, 12, 13, 14]

num = [10, 11, 12, 13, 14]
even_num = filter(lambda x: x % 2 == 0, num)
print(list(even_num)) 