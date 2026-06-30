a = input("Enter 1st no.:")
a = int(a) # In this line we are converting the string into integer using int() function.
# Because the input() function takes the input as a string by default, we need to convert it into integer to perform the arithmetic operation.
print(a + 3) 

a = input("Enter 1st no.:")
b = input("Enter 2nd no.:")
c = int(a) + int(b)
print(c)

# And in better way :

a = int(input("Enter 1st no.:"))
b = int(input("Enter 2nd no.:"))
c = a + b
print(c)