'''4. Write a program to demonstrate string 
operations including slicing formatting and 
built-in string functions.'''

text = "python programming"
print("Original String:", text)
print()

print("text[0:6]:", text[0:6])
print("text[:6]:", text[:6])
print("text[6:]:", text[6:])
print("text[::2]:", text[::2])
print("text[::-1]:", text[::-1])
print("text[:-1]:", text[:-1])
print()

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Capitalized:", text.capitalize())
print("Length:", len(text))
print("Split:", text.split(" "))
print("Replace 'p' with 'l':", text.replace("p", "l"))
print("Swapcase:", text.swapcase())
print("Position of 'thon':", text.find("thon"))

