''' 8. Write a program to explain mutable and 
immutable objects in Python. '''

print('List Is Mutable')
list = [10,20,30,40,50,90,100]
print(list)
print()

#append
print('value added')
list.append(60)
print(list)
print()

#remove
print('remove the value')
list.remove(40)
print(list)
print()

print('------------------------------------------')

print('Set Is Mutable')
set = {2,5,4,6,7,3,1,9}
print(set)
print()

#add
print('value added')
set.add(8)
print(set)
print()

#remove
print('remove the value')
set.remove(9)
print(set)
print()

print('------------------------------------------')

print('Dict Is Mutable')
dict = {'name':'Bhargav',
           'rollno':4065,
           'div':'A'}
print(dict)
print()

#add
print('value added')
dict['field'] = 'MCA'
print(dict)
print()

#remove
print('remove the value')
dict.pop('div')
print(dict)
print()

print('------------------------------------------')

print('Tuple Is Immutable')
tuple = (10,20,30,40,50,90,100)
print(tuple)
print()

print('values not added and removed in tuple')



