''' 41. Write a program to demonstrate different types
of errors and exceptions in Python. '''

try:
    compile("if True print('Hello')", "<string>", "exec")
except SyntaxError:
    print("SyntaxError: invalid syntax")

try:
    print(10 / 0)
except ZeroDivisionError:
    print("ZeroDivisionError: division by zero")

try:
    print(x)
except NameError:
    print("NameError: variable is not defined")

try:
    print("10" + 5)
except TypeError:
    print("TypeError: unsupported operand type")

try:
    int("abc")
except ValueError:
    print("ValueError: invalid value")

try:
    a = [10, 20, 30]
    print(a[5])
except IndexError:
    print("IndexError: list index out of range")
