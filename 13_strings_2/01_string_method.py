#Strings are immutable.

s = "hello world"

# name[0] = "o"  # You cannot do this

#len() - Get Length of a String
a = len(s)
print(a)

#Changing Case:

print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())

#Removing Whitespace:

text = "  hello world  "
print(text.strip()) 
print(text.lstrip()) 
print(text.rstrip())

# Finding and Replacing

text = "Python is fun"
print(text.find("is")) 
print(text.replace("fun", "awesome")) 

# Splitting and Joining

text = "apple,banana,orange"
fruits = text.split(",")
new_text = " - ".join(fruits)
print(new_text) 

#    OR

text = "apple,banana,orange"
print(text.split(","))
print(",".join(['apple', 'banana', 'orange']))

# Checking String Properties

text = "Python123"
print(text.isalpha()) # Output: False
print(text.isdigit()) # Output: False
print(text.isalnum()) # Output: True
print(text.isspace()) # Output: False


