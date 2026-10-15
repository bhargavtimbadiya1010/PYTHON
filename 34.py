''' 34.Write a program to demonstrate instance 
methods class methods and static methods. '''

class student:
    subject = 'Python'


    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self,sub):
        print("name is: ",self.name)
        print("age is: ",self.age)
        self.subject = sub
        print(self.subject)

    @classmethod
    def sub(cls):
        print("Subject is: ",cls.subject)

    @staticmethod
    def message():
        print('hello students')

s1 = student('bhargav',21)
s1.display('abc')
s1.sub()

s2 = student('jalpit',29)
s2.display('xyz')
s2.sub()

s1.message()
