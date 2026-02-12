''' Encapsulation = controlling access to data
In real systems, you never allow direct access to critical data.
Why Encapsulation Exists:
1. Protect sensitive data
2. Prevent accidental modification
3. Improve maintainability
4. Enforce business rules
'''
# Public

class User:
    def __init__(self, name):
        self.name = name #

u = User("Azeem")
print(u.name)

# Protected (_)

class User:
    def __init__(self, name):
        self._name = name #

class Admin(User):
    def show(self):
        print(self._name)

a = Admin("Azeem")
a.show()

# Private (__) 

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance #

    def show_balance(self):
        print(self.__balance)

acc = BankAccount(10000)
acc.show_balance()