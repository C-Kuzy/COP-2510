'''
 Author: Connor Kouznetsov
 Description: Lecture Notes
'''

#multipe inputs will show using a split
a,b = input('Enter 2 values (separated by space):').split()
print(f'You entered {a} and {b}.')

a = int(a); b = int(b)

c = a + b
print(f'{a} + {b} = {c}.')

#How we focus on importing modules

import math, random
sqrt = math.sqrt(b)
print(f'The square root of {b} = {sqrt}.')

m = random.randint(1, 6)
print(f" Here's a random integer between 1 and 6 (incl.): {m}.")

#import method from a module

from math import cell, trunc
ce = ceil(b)
tr = trunc(b)

print(f'{b} using cell is {ce}.')
print(f'{b} using trunc is {tr}.')

#Importing all methods from modules using * (this is a wildcard)
#This will only work with one module at a time
from math import *
f = fabs(b)
print('The absolute value of {b} is {f}).')

#Advice: Don't import all methods in this way...
#from math import *
#from random import *
#from matplotlib import *

#Create an alias to rename a method
from random import random as rand
r = rand()
print(r)

#Create an alias to rename a module
import random as rn
r2 = rn.rand()
print(r2)
r3 = rand()
r4 = rn.rand()

x=random
print(x)