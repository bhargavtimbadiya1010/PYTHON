'''43.Write a program to define and raise userdefined exceptions.'''

age = int(input("Enter the age: "))

class InvalidAgeError(Exception):
    pass

try:
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")

    print("Eligible to vote")

except InvalidAgeError as e:
    print("Custom Exception:", e)
