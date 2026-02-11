'''What is Hierarchical Inheritance?
One parent class → multiple child classes'''
# Project: Bank Account System (Hierarchical)

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display(self):
        print(f"Account No.: {self.account_number}")
        print(f"Balance: {self.balance}")


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        self.display()
        interest = self.balance * (self.interest_rate / 100)
        print(f"Annual Interest Earned: {interest}")
        return interest


class CurrentAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def check_limit(self, withdrawal_amount):
        total_available = self.balance + self.overdraft_limit
        if withdrawal_amount > total_available:
            print(f"Declined: Exceeds overdraft limit of {self.overdraft_limit}.")
            return False
        else:
            print("Transaction Successful")
            return True

savings = SavingsAccount(125, 10000, interest_rate=5)
savings.calculate_interest()

current = CurrentAccount(125, 10000, 200)
current.check_limit(5000)