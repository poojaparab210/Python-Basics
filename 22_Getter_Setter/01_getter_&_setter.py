

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    # Python provides a more elegant and concise way to implement getters and setters using the @property decorator. This allows you to access and modify attributes using the usual dot notation (e.g., p.name ) while still having the benefits of getter and setter methods.
    def first_name(self):
        l = self.name.split(" ")
        return l[0]
    
    @first_name.setter
    # def set_first_name(self,first):
    def first_name(self,first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name

e = Employee("Jack Deo",35000)
# print(e.first_name())
# e.set_first_name("John")
# print(e.name)

print(e.first_name)
e.first_name = "John"
print(e.name)