#F2024Week2Lec2
#REMEMBER, YOU WILL NEED TO ADD THE FOLLOWING INTO EACH PROGRAMMING ASSIGNMENT
"""
 Author: Connor Kouznetsov
 UNumber: U#########
 Description: Thursday's Notes, Tips & Tricks
"""

#v1=3.5;v2=10 #; is used to separate multiple statements on a single line

v1=int(input('Enter an integer:'))
v2=float(input('Enter a floating point number:'))
name = input('Enter a name')
print('Here are the values: v1 is', v1, ',v2 is', v2, sep ='')
print(f'Here are the values: v1 is {v1}, v2 is {v2}')
v3=v1+v2
print(f'v3 is {v3}')
print(f'name is {name}')

#multiple assignment
n1=n2=n3=0
print(f'n1 is {n1}, n2 is {n2}, and n3 is {n3}')

#respective assignment
n4, n5 = float(input()),int(input)
print(f'n4 is {n4} and n5 is {n5}')

#use a tuple as a 'constant,'
MAX=(400,)
print(MAX[0])

#enotation & formatting
mm_jackpot= 7.4e8
print(f"Friday's Mega Millions jackpot is ${mm_jackpot:,.2f}")

#walrus operator:=
print('v1 is', v1:=int(input()))

#The line above is equivalent to the two lines above
v1=8
print('v1 is now', v1)

print (f'v1 is now {v1:=15}') #creates a field width that is the size of the value input

#The following are Math Operators: +, -, *, /, //, %, **
# + = Addition
# - = Subtraction
# * = Multiplication
# / = Division
# // = Remainder
# % =
# ** = Exponents

#THIS THE ORDER YOU SHOULD TAKE WITH MATH OPERATORS
#1.() = Parenthesis
#2. ** = Exponents
#3. *, /,
#4. +, -, 

