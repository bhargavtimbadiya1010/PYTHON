''' 10.Write a program to demonstrate recursion using 
factorial or Fibonacci series. '''

num = int(input('Enter the Number: '))
ans = 1

#simple
for i in range(1,num+1):
    ans*=i
print(ans)

#recursion    
def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fact(num-1)

ans = fact(num)
print()
print("Factorial Demonstration")
print(f"The factorial of {num} is: {ans}")
print('---------------------------------')

# Simple Fibonacci
a = 0
b = 1

for i in range(num):
    a, b = b, a + b
print(b)

# Recursion Fibonacci
def fib(num):
    if num <= 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

ans = fib(num)
print()
print("Fibonacci Demonstration")
print(f"The Fibonacci value of {num} is: {ans}")


