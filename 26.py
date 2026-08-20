''' 26.Write a program to perform file and directory 
operations using os and sys modules. '''

import os
import sys

print(sys.version)

os.makedirs('bhargav')
print('Directory Created')

checkdir = os.path.dirname('D:\\bhargav-4065\\python\\20.py')
print('Directory name:',checkdir)

check = os.path.isfile('D:\\bhargav-4065\\python\\20.py')
print('File found in the folder or not:',check)

os.rename('pro20.py','20.py')
os.remove('ex.py')

bname = os.path.basename('D:\\bhargav-4065\\python\\20.py')
print('File path Basename:',bname)

absolute = os.path.isabs('D:\\bhargav-4065\\python\\20.py')
print('File path Absolute or not:',absolute)



