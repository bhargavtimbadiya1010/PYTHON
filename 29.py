''' 29.Write a program to use re module functions 
such as match search and find all. '''

import re

txt = 'use re module functions such as match search and find all match'

match = re.search(r'such',txt)

if match:
    print('match found:',match.group())
else:
    print('match not found')
    

find = re.findall(r'match',txt)

if find:
    print('match found:',find)
else:
    print('match not found')
