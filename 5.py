'''5. Write a program to create and manipulate lists 
using indexing slicing and list comprehensions. '''

text = ['apple', 'banana', 10, 'cherry', 'orange', 20, 'grapes', 'kiwi']
print("Original List:", text)
print()

print("First Element:", text[0])
print("Third Element:", text[2])
print("Last Element:", text[-1])
print()

print("text[0:7]:", text[0:7])
print("text[:7]:", text[:7])
print("text[5:]:", text[5:])
print("text[::2]:", text[::2])
print("text[::-1]:", text[::-1])
print("text[:-1]:", text[:-1])
print("text[1:6:2]:", text[1:6:2])
print()

text.pop(2)
print("After removing element at index 2:", text)

text.append("lemon")
print("After adding lemon:", text)

text.reverse()
print("After reversing:", text)

numbers = [1, 2, 3, 4, 5, 6]
squares = [num ** 2 for num in numbers]

print("Numbers:", numbers)
print("Squares:", squares)

text.clear()
print("After clearing the list:", text)





