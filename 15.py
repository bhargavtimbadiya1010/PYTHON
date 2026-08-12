'''5.Write a program to demonstrate the use of 
break continue and pass statements.'''

print('Break')
for i in range(1,6):
    if i==2:
        break
    print(i)

print('---------')

print('Continue')
for i in range(1,6):
    if i==2:
        continue
    print(i)

print('---------')

print('Pass')
for i in range(1,6):
    pass
