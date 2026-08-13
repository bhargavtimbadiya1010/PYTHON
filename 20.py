'''20.Write a program to generate a sequence of 
numbers using generator functions and yield 
keyword. '''

def gen(n):
    while n > 0:
        yield n
        n-=1

for n in gen(7):
    print(n)
