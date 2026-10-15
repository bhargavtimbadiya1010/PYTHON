''' Write a program to demonstrate constructor
and destructor usage. '''

class python:

    def __init__(self):
        print("constructor called")
        print("python object created")

    def __del__(self):
        print("destructor called")
        print("python object created")

p1 = python()
p1.__del__()
