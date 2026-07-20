# The walrus operator (:= ), introduced in Python 3.8, is an assignment expression operator. It allows you to assign a value to a variable within an expression. This can make your code more concise and, in some cases, more efficient by avoiding repeated calculations or function calls. The name “walrus operator” comes from the operator’s resemblance to the eyes and tusks of a walrus.

def very_slow_func():
    print("Something.......")
    print("Something.......")
    print("Something.......")
    print("Something.......")
    print("Something.......")
    return 70

# a = very_slow_func()
if((a:=very_slow_func())>10):
    print(a)
else:
    print("Its not greater than 10")


#               or

while(data:=input("Enter the value:")):
    print(data)
    if data == "q":
        break