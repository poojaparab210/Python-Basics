# Create a class Employee with private attribute _salary.
# 1. Use @property to define getter for salary
# 2. Use @salary.setter to prevent setting negative values(print a warning instead)
# 3. Create an object and test by setting positive and negative salaries.

class Employee:
    def __init__(self,salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,value):
        if value<0:
            print("Oops its is negative")
        else:
            self._salary = value
    
e = Employee(3)
e.salary = 67
print(e.salary)

    
