'''What is Multiple Inheritance?
When one child class inherits from more than one parent class.

MRO - Method Resolution Order:
MRO decides which method is called first in multiple inheritance.
Python Rule:

* Left-to-right order
* Uses C3 Linearization algorithm'''
# Project: Authentication System

class User:
    def __init__(self,user_name):
        self.user_name = user_name

    def login(self):
        return self.user_name

class Admin:
    def __init__(self,admin_level):
        self.admin_level = admin_level

    def login(self):
        return self.admin_level
    
class SuperAdmin(User, Admin):
    def __init__(self, user_name, admin_level):
        User.__init__(self, user_name)
        Admin.__init__(self, admin_level)

    def login(self):
        return "SuperAdmin Login"
    
sa = SuperAdmin("Azeem","High")
print(sa.login())