

class Employee:
    company = "Asus"   # This is class attributes

    def __init__(self, salary, name, bond, company):
        self.salary = salary   # create an instance attribute of name salary assign it with salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):   
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}.\nSalary is {self.salary}.\nThe bond is for {self.bond} years")
    
e1 = Employee(34000, "John Deo", 4, "Tesla")
print(e1.company)  # Will always print instance attribute whenever present
print(Employee.company) # This will always print class attribute 

# Object introspection
print(dir(e1))
