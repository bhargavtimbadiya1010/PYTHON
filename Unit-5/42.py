'''42.Write a program to handle exceptions using try
except else and finally blocks.'''

a = int(input("Enter value a: "))
b = int(input("Enter value b: "))

try:
    result = a / b

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Division =", result)

finally:
    print("Finally block always executes")
