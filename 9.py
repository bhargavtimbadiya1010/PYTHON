''' Write a program to define and use user-defined 
functions with different types of arguments. '''

a = int(input('Enter value A: '))
b = int(input('Enter value B: '))
op = input('Enter the operation(+,-,*,/): ')

def cal(a,b,op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        return a/b
    else:
        print('Invalid operation')

print(cal(a,b,op))
    
