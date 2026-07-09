def sum(a,b):
    # a and b are local variables
    c = a+b
    z = 1 # It create a local variable called z which is destroy after this fuction returns.
    return c

def greet():
    z = 32 # Local variable
    print("hello")
z = 8 # z is a global variable 
print(sum(4,6))
print(z)



