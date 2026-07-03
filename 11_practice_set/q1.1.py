# Write a program that asks the user for a number and prints whether it is positive, negative, or zero.

num = int(input("Enter 1st no : "))
if num > 0:
    print("It is a positive number.")
elif num < 0:
    print("It is a negative number.")
else:
    print("It is zero.")