# Project Name: Student Management System
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print(self.name, self.roll_no, self.marks)

        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")

s1 = Student("Azeem", 19, 90)
s1.display()
