# Write a function print_details(**kwargs) that print key-value pairs passed as arguments

def print_details(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Jack",age =21, city="Delhi")