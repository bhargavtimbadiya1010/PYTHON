'''Write a program to create a dictionary and 
demonstrate dictionary methods and iteration. '''

student = {
    'name': 'Bhargav',
    'rollno': 4065,
    'div': 'A'
}

print("Dictionary:", student)
print("Type:", type(student))
print("Name:", student["name"])
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Removed Value:", student.pop('div'))
print("Dictionary after pop:", student)

print("\nDictionary Iteration:")
for key, value in student.items():
    print(key, ":", value)