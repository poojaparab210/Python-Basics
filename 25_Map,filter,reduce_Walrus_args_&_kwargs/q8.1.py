# Write a function sum_all(*args) that accept any number of integer and return their sum

def sum_all(*args):
    print(type(args))
    sum = 0
    for item in args:
        sum += item
        
    return sum
print(sum_all(1,2,3,4,5))