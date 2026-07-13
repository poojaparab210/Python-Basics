# Write a program that takes a list of numbers and removes all duplicates using a set.

def remove_duplicates(numbers):
    return list(set(numbers))

num = [1,2,3,2,4,1,6,7,6,8]
print("Original List:",num)
print("Without Duplicates:",remove_duplicates(num))