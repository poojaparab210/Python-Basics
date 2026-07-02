# Match Case Statements in Python (Python 3.10+)

# Match-case is a new feature introduced in Python 3.10 for pattern matching.
# It simplifies complex conditional logic.

a = int(input("Enter a number between 1 and 10:"))

match a:
    case 1:
        print("You won a charger")
    case 7:
        print("You won a pen")
    case 3:
        print("You won a notebook")
    case 5:
        print("You won a book")
    case 10:
        print("You won a car")
    case _:
        print("Better luck next time!")
    
