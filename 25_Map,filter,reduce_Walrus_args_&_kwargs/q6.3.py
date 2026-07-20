# Use reduce() from functools to find the product of all element in [1, 2, 3, 4]

from functools import reduce

numbers = [1, 2, 3, 4]
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print(product_of_numbers) 