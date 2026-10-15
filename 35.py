''' 5. Write a program to implement single , multilevel 
and multiple inheritance. '''

class A:
    name1 = 'het'

class B(A):
    name2 = 'ravi'

class C(B):
    name3 = 'mahesh'


class D:
    name3 = 'raju'

class E(D,C):
    pass


#single

#ob1 = B()
#print(ob1.name1)

#multilevel

ob2 = C()
print(ob2.name2)
print(ob2.name3)
print(ob2.name1)

#multiple

#ob3 = E()
#print(ob3.name2)
#print(ob3.name3)
#print(ob3.name1)


    








