'''Polymorphism is the ability of different objects to respond to the 
same method call in their own specific ways.
* Same method name,
* Different behavior,
* Depending on the object.'''
# Method Overriding:
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Cash")

payments = [
    CreditCardPayment(),
    UPIPayment(),
    CashPayment()
]

for payment in payments:
    payment.pay(500)