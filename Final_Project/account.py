from exceptions import InsufficientBalanceError, InvalidAmountError


class Account:

    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self._balance = balance   # Encapsulation

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive")

        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive")

        if amount > self._balance:
            raise InsufficientBalanceError("Insufficient balance")

        self._balance -= amount

    def get_balance(self):
        return self._balance

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self._balance
        }
if __name__ == "__main__":
    a = Account("101", "Azeem", 5000)
    a.deposit(1000)
    print(a.get_balance())


