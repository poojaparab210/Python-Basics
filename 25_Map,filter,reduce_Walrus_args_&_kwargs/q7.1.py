# Use the walrus operator to read input the user enter "quit" . Print each input as it is entered

while (data := input("Enter a value: ")) != "quit":
    print(f"You entered: {data}")