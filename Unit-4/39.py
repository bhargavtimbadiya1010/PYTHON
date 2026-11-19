'''39. Write a program to read and write data into a
file using different file modes.'''

f = open("student.txt", "w")
f.writelines(["Hello Python\n","Marwadi University\n","File Handling"])
f.close()

f = open("student.txt", "r")
print(f.read())
f.close()

f = open("student.txt", "a")
f.write("\nWelcome to Python")
f.close()

f = open("student.txt", "r")
print(f.read())
f.close()