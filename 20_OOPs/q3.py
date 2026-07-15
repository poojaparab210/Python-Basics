# Create a base class Animal with a method sound() that prints "Some sond" . Create a derived class Dog that overrides sound() to print "bark!" . Create an object of Dog and call sound().

class Animal:
    def sound(self):
        print("Some sound...")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Bark!!!")

d = Animal()
d.sound()

b = Dog()
b.sound()