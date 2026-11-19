'''38. Write a program to demonstrate encapsulation
and abstraction using classes. '''

from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def interest(self):
        pass

class Account(Bank):
    def __init__(self, balance):
        self.__balance = balance

    def interest(self):
        print("Interest rate is 5%")

    def show_balance(self):
        print("Balance:", self.__balance)


obj = Account(10000)
obj.show_balance()
obj.interest()