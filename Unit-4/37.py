'''37. Write a program to illustrate method resolution
order and magic methods.'''

class A:
    def Display(self):
        print('Class A')

class B(A):
    def Display(self):
        print('Class B')

class C(B):
    pass

class Number:
    def __init__(self,n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n 

obj = C()
obj.Display()

print("MRO:", C.mro())

n1 = Number(10)
n2 = Number(20)

print("Addition:", n1 + n2)