''' 9.Write a program to demonstrate iterators and 
iterables in Python. '''

fruits = ["apple", "banana", "cherry", "kiwi"]

fruit_iter = iter(fruits)
print('iterator:')
print(next(fruit_iter))  
print(next(fruit_iter))  
print(next(fruit_iter))
print(next(fruit_iter))

print('------------------')

l = [1,2,3,4,5]
print('iterables:')
for i in l:
    print(i)
