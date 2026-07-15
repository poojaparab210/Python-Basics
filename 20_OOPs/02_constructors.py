


class Employee:

    def __init__(self, salary, name, bond):
        self.salary = salary   # create an instance attribute of name salary assign it with salary
        self.name = name
        self.bond = bond

    def get_salary(self):   
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}.\nSalary is {self.salary}.\nThe bond is for {self.bond} years")
    
e1 = Employee(34000, "John Deo", 4)
# print(e1.get_salary())
e1.get_info()
