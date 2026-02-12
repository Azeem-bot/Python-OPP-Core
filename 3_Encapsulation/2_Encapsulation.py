# Encapsulation is achieved by keeping balance private and
# allowing access only through controlled methods like deposit and withdraw.

# Project: Secure Bank Account 

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


bank_acc = BankAccount(8000)
bank_acc.deposit(2000)
bank_acc.withdraw(3000)
print("Balance:", bank_acc.get_balance())