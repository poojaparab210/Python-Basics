# Write a program that keeps asking the user to enter a password until they enter the correct one.

i = "AB123"
enter_pass = input("Enter a password:")
while (enter_pass != i) :
    enter_pass = input("Try again:")
print("Successfully! looged in")