# Project Name: Bank Account Management System
class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")
        print(f"Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
            print(f"Balance: {self.balance}")

    def display(self):
        print(f"Name: {self.account_holder}")
        print(f"Account No: {self.account_number}")
        print(f"Balance: {self.balance}")
