# Write a program that asks the user to enter a number and handles ValueError is the input is not zero and ZeroDivisionError if you try to  divide by zero
#  Create a custom exception NegativeNumberError and raise it when the user enter negative number

class NegativeNumberError(Exception):
    pass
try:
    num = int(input("Enter a number: "))
    if num<0:
        raise NegativeNumberError("Number cannot be negative")
    result = 45 / num
    print(f"The result is {result}")
except ZeroDivisionError:
    print("Error:You can't divide by zero!")
except ValueError:
    print("Error:Invalid input! Please enter a number.")
except NegativeNumberError as e:
    print(f"Error : {e}")