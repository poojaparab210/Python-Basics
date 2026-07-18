
while True:
    try:
        a = int(input("Enter no 1 :  "))
        b = int(input("Enter no 2 : "))
        print(f"The Division is {a/b}")
    except ValueError:
        print("Please donot perform bad typecaste")
    except ZeroDivisionError:
        print("Hey donot divide by 0")
    except Exception as e:
        print("Unknown error occurred!",e)



# Raise :


# a = int(input("Enter no 1 :  "))
# b = int(input("Enter no 2 : "))

# if b == 0:
#     raise ValueError("Please dont divide by 0")
    
# print(f"The Division is {a/b}")