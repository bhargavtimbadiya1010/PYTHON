''' 28. Write a program to demonstrate basic regular 
expression pattern matching.''' 
import re

s = input("Enter mobile number: ")

regular_expression = re.compile(r'\d{10}')

ans  = regular_expression.search(s)

if ans == None:
    print("not a valid number")
else:
    print("mobile number: ",s)
