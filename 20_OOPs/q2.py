# Create a class Person with a constructor (__init__) that accept name and age as arguments and store them as instance attributes.Create an object and print the person's name and age.

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def get_info(self):
    #     print(f"The name is {self.name}.\nThe age is {self.age}.")

p1 = Person("Pooja",21)
print(p1.name, p1.age)