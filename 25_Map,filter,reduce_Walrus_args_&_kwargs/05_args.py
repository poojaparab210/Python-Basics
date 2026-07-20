# *args and **kwargs are special syntaxes in Python function definitions that allow you to pass a variable number of arguments to a function. They are usedwhen you don’t know in advance how many arguments a function might need to accept.
# • *args : Allows you to pass a variable number of positional arguments. 
# • **kwargs : Allows you to pass a variable number of keyword arguments.

def sum (*args):
    # args will be tuple of all the values passed to sum.
    total = 0
    for item in args:
        total += item
    return total

print(sum(342, 2, 7))
