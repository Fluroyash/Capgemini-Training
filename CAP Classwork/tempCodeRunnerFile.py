class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)   
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)



m1 = Manager("Yash", 100000, "IT")
m2 = Manager("Nehal", 90000, "HR")

m1.display()
print()
m2.display()