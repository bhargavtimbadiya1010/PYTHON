''' 27.Write a program to copy move and delete files 
using shutil module.'''

import shutil
import os

if os.path.isfile('1.py'):
    if not os.path.isdir('pydir'):
        os.makedirs('pydir')
    shutil.copy('1.py','pydir')
    if not os.path.isdir('bhargav'):
        os.makedirs('bhargav')
    shutil.move('D:\\bhargav-4065\\python\\pydir\\1.py','bhargav')
    
    os.remove('bhargav\\1.py')

