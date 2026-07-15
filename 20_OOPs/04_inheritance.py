

class Animal:   # Parent Class (superclass)
    location = "Australia"

    def __init__(self,name):
        self.name = name

    def speak(self):
        print("Speaking now......")

class Dog(Animal):   # This is how inheritance is done in Python
    def speak(self):
        super().speak()   # We are using the speak function of the parent class.
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

# a = Animal("Dog")
# a.speak()

d = Dog("Rocky")
d.speak()
print(d.location)

c = Cat("Mimi")
c.speak()