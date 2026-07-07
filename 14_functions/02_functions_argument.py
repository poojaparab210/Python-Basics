# Functions can take parameters and return values.

# Types of Arguments:
# 1. Positional Arguments

def add(a,b):
    return a+b
c = add(3,5)
print(c)

# 2.  Default Arguments

def add(a,b,plus=0):
    x = a+b+plus
    return x
c = add(3,5,2)
print(c)

# 3.  Keyword Arguments

def add(a,b,plus=0):
    x = a+b+plus
    return x
c = add(b=3,a=5)
print(c)
