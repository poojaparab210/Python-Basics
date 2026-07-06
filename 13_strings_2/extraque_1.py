# Write a program that counts how many vowels are in a given string.

text = "A Coding in Python is fun. A python is beginner friendly for everyone."
sum = 0
vowels = ['a','e','i','o','u']
for char in text:
    if(char in vowels):
        sum += 1
print(f"There are {sum} vowels in this sentence.")