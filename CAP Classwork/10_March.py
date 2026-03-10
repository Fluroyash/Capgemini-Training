
"""""
class Parent:
    def show(self):
        print("This is Parent class method")

class Child(Parent):
    def display(self):
        print("This is Child class method")
        super().show()   # calling parent class method

obj = Child()
obj.display()

"""


"""
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


"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @property
    def result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"


s1 = Student("Yash", 55)

print(s1.name)
print(s1.result)   