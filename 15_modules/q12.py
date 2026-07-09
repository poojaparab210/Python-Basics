# write a function multiply(a,b) that has a proper docstring explaning what it does.Then use help(multiply ) to display the docstring

def multiply(a,b):
    '''
    Multiply two numbers.

    Parameters:
    a ,b : this two parameters are in int or float

    returns:
    int or float : The product of a and b
    '''
    c = a * b
    return c
print(multiply(6,9))
help(multiply)