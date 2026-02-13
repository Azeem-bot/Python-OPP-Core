# Project: Payment System
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount: float):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount: float):
        print(f"Paid {amount} using Credit Card")


class UPIPayment(Payment):
    def pay(self, amount: float):
        print(f"Paid {amount} using UPI")


cc = CreditCardPayment()
upi = UPIPayment()

cc.pay(500)
upi.pay(1000)