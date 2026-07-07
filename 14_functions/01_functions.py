# a = 5
# b = 2
# c = 1

# average = (a + b + c)/3
# print(average)

# Functions help in reusability and modularity in Python. 
# Defined using def keyword.
# Function name should be meaningful.
# Use return to send a value back.

def average(a,b,c):
    d = (a + b + c)/3.0
    # print(d)
    return d
o1 = average(3,5,1)
o2 = average(4,2,1)
print(o1)
print(o2)