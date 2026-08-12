'''Write a program to demonstrate conditional 
statements using if if-else and if-elif-else.'''

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
