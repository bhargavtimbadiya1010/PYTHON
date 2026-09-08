''' 30.Write a program to extract specific information 
from a text file using regular expressions. '''

import re

with open('30.txt','r') as d:
    extract = d.read()
    regular_exp = re.compile(r'b\w+')
    
    match = regular_exp.findall(extract)
    print('match found: ',match)

