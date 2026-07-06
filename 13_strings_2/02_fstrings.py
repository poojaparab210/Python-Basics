# String formatting
#format() and f-strings

template = "Dear {}, You are awesome. Take this {}$ bag"
a = "John"
a1 = 10000
b = "Jack"
b1 = 1000
c = "Marie"
c1 = 300

# Using .format() Method:
# The .format() method allows inserting values into placeholders {} :

s1 = template.format(a ,a1)
print(s1)

# f-Strings (Formatted String Literals)
# Introduced in Python 3.6, f-strings are the most concise and readable way to format strings:
print(f"{a} you are awesome and take this {a1}$ bag")

# Using Expressions in f-Strings
# You can perform calculations directly inside f-strings:

x = 10
y = 5
print(f"The sum of {x} and {y} is {x + y}")

# Formatting Numbers
pi = 3.14159265
print(f"Pi rounded to 2 decimal places: {pi:.2f}")

# Padding and Alignment
text = "Python"
print(f"{text:>10}") # Right align
print(f"{text:<10}") # Left align
print(f"{text:^10}") # Center align