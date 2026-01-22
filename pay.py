

from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def process_payment(self):
        print("Оплата")


class CreditCardPaymement(Payment):
    def process_payment(self):
        return "Оплата кредитной картой"


class StripePayment(Payment):
    def process_payment(self):
        return "Оплата Stripe"


class PayPalPayment(Payment):
    def process_payment(self):
        return "Оплата PayPal"


payments = [
    CreditCardPaymement(),
    StripePayment(),
    PayPalPayment(),

]


for payment in payments:
    payment.process_payment()
    print(payment.process_payment())
