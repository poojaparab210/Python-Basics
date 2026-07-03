# Write a program using match case that simulates a simple calculator.
# 1.Ask the user for two numbers and an operation (+, -, *, /).
# 2. Perform the operation using match case 

num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
operation = input("Choose operation:")
match operation:
    case "+" :
        print(num1 + num2)
    case "-" :
        print(num1 - num2)
    case "*" :
        print(num1 * num2)
    case "/" :
        print(num1 / num2)
    case _ :
        print("Invalid operation")