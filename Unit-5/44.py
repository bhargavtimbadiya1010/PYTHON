'''44.Write a program to demonstrate the use of
assert statement. '''

marks = int(input("Enter the marks: "))

try:
    assert 0 <= marks <= 100, "Marks must be between 0 and 100"
    print("Valid Marks")

except AssertionError as e:
    print("AssertionError:", e)
