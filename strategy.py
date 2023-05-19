# Strategy Pattern - Allows one of a family of algorithms to be selected on-the-fly at run-time
# https://www.youtube.com/watch?v=Nrwj3gZiuJU&list=PLlsmxlJgn1HJpa28yHzkBmUY-Ty71ZUGc

from abc import ABC, abstractmethod
from typing import Final

# =============================================
class CreditCard:
    def __init__(self,number,expiry_date,cvv) -> None:
        self.amount = 1000
        self.number: Final = number
        self.expiry_date: Final = expiry_date
        self.cvv: Final = cvv
    
    def get_amount(self):
        return self.amount

    def set_amount(self,amt):
        self.amount = amt

# =============================================
# Strategy Interface
class IPaymentStrategy(ABC):    
    @abstractmethod
    def collect_payment_details(self):
        pass

    @abstractmethod
    def validate_payment_details(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass

# Concrete Strategy 
class PaymentByCreditCard(IPaymentStrategy):
    def __init__(self):
        self.card = None
    
    def collect_payment_details(self):
        self.card = CreditCard("1234-5678","02-18-2023","123")
        
    def validate_payment_details(self):
        return True
    
    def pay(self, amount):
        print(f"Paying", str(amount), "using Credit Card")
        self.card.set_amount(self.card.get_amount() - amount)

class PaymentByPayPal(IPaymentStrategy):
    def __init__(self):
        self.email = None
        self.password = None

    def collect_payment_details(self):
        self.email = ""
        self.password = ""
        
    def validate_payment_details(self):
        return True
    
    def pay(self, amount):
        print(f"Paying", str(amount), "using PayPal")

# =============================================
class PaymentService:
    def __init__(self, strategy, cost, is_delivery = False) -> None:
        self.strategy = strategy
        self.cost = cost
        self.include_delivery = is_delivery

    def process_order(self):
        self.strategy.collect_payment_details()
        if self.strategy.validate_payment_details():
            self.strategy.pay(self.get_total())

    def get_total(self):
        return self.cost + 10 if self.include_delivery else self.cost

# =============================================
# Client
credit_card = PaymentByCreditCard()
payment_service = PaymentService(credit_card, 100, True)
payment_service.process_order()

paypal = PaymentByPayPal()
payment_service = PaymentService(paypal, 100)
payment_service.process_order()