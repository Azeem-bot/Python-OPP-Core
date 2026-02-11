'''What is Inheritance?
Inheritance allows one class to reuse properties and methods of another class.

1. Parent class (Base class) → gives features
2. Child class (Derived class) → receives & can extend features'''
# Employee System

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary} per month")


class Developer(Employee):
    def __init__(self,name,salary,programming_lang):
        super().__init__(name,salary)
        self.programming_lang = programming_lang

    def display_details(self):
        self.display()
        print(f"Programming Language: {self.programming_lang}")

# employee1 = Employee()
# employee1.display()
dev = Developer(name="Azeem", salary=150000, programming_lang="Python")
dev.display_details()