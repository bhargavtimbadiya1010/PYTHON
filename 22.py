''' 22.Write a program to demonstrate different 
import mechanisms in Python. '''

import mymodule
mymodule.name('bhargav')

print('------------------------')

from mymodule import name
name('jalpit')

print('------------------------')

from mymodule import name as n
n('rajdeep')

print('------------------------')

import mymodule as nm
nm.name('jay')

print('------------------------')

from mymodule import *
name('suresh')
enro(4065)

print('------------------------')
