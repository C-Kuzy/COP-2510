#Fall2024 Week 2 Lecture 1

"""
 Author: Connor Kouznetsov
 Description: Tuesday Notes, Tips, and Tricks
"""

#The following code is strictly not a comment but you can use it as one:
'''Students tend to use this string
... as a comment within their code.'''


#Use of the sep and end parameters in print function
print('cdkouznetsov','usf.edu')
print('cdkouznetsov','usf.edu',sep='@',end='')
print('','Use this email to log in!')

#The use of Variables, Identifier Rules and F-Strings
import math
import random
import turtle

#declare - create a variable
#initialize - the first time you assign a value to a variable
# = is your assignment operator

var=6
rate=9.7
string_name='value'
switch=True
variableName=3.4#camelnaming

#echoprint the values in the variables
print('Here are the values: var is', var,',rate is', rate,',string_name is', string_name,'and switch is', switch)
print(f'Here are the values var is {var}, rate is {rate}, string_name is {string_name}, and switch is {switch}')#print with f-string
#print('Here are the values{var}{rate}{string_name}{switch}')

#effect of a variable (In Python)
var=9.4
rate='discount'
string_name=False
switch=8

print(f'Here are the values var is {var}, rate is {rate}, string_name is {string_name} and switch is {switch}')

#for a 'constant' in Python, declare a variable (using upper case letters) ... and insure you leave it alone
MAX_SEATS = 459
