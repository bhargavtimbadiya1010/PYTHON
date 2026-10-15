''' 33. Write a program to illustrate instance variables 
and class variables. '''

class car:
    company = 'BMW'
    def __init__(self,carnm,colour):
        self.carnm = carnm
        self.colour = colour

    def show(self):
        print("Car name is: ",self.carnm)
        print("Car colour is: ",self.colour)
        
    @classmethod
    def companynm(cls):
        print("Company name:",cls.company)

c1 = car('M5 Competition','Silver')
c1.show()
c1.companynm()

        
        
