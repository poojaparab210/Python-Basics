# Take a user input string and check if it is a palindrome (same forwards and backwards)

user = input("Enter the name:")
if (user == user[::-1]):
    print("Yes! It is palindrome")
else:
    print("No!!")