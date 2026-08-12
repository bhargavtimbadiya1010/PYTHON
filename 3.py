'''3. Write a program to perform arithmetic 
relational and logical operations using Python 
operators.'''

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

#arithmatic operation
print("Sum is: ",a+b)
print("Substraction  is: ",a-b)
print("Multiplication is: ",a*b)
print("Division is: ",a/b)
print("Reminder is: ",a%b)
print()

#relational operation
print("a == b : ",a==b)
print("a > b : ",a>b)
print("a < b: ",a<b)
print("a != b: ",a!=b)
print("a >= b: ",a>=b)
print("a <= b: ",a<=b)
print()

#logical operation
print("a>b && a<b : ",(a>b)and(a<b))
print("a>b && a=b : ",(a>b)or(a==b))
print("a>b && a<b : ",not(a>b))







