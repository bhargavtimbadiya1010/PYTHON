'''6.Write a program to iterate over lists strings and 
dictionaries using loops. '''

l = [10,20,30,40,50]

s = "Marwadi University"

d = {1:'Bhargav',2:'Het',3:'Jalpit',4:'Bapu'}


print('iterating list')
for i in l:
    print(i)
    
print('------------------------')

print('iterating string')
for i in s:
    print(i)

print('------------------------')

print('iterating dictionary')
for i,j in d.items():
    print('key',i,'values',j)

print('------------------------')
