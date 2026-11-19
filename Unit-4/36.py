'''6. Write a program to demonstrate method
overriding and polymorphism. '''

class Payment:
    def pay(self):
        print("Payment completed")


class UPIPayment(Payment):
    def pay(self):
        print("Payment completed using UPI")


class CardPayment(Payment):
    def pay(self):
        print("Payment completed using Card")


upi = UPIPayment()
card = CardPayment()
pmt = Payment()

upi.pay()
card.pay()
pmt.pay()
