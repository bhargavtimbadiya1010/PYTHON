'''40.Write a program to perform file pointer
operations using seek and tell methods. '''

f = open("student.txt", "w")
f.write("File Pointer Operations")
f.close()

f = open("student.txt", "r")

print("Current position:", f.tell())

print("Data:", f.read(7))
print("Current position:", f.tell())

f.seek(0)
print("Position after seek:", f.tell())

print("Data:", f.read())

f.close()