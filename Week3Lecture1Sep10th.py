'''
 Author: Connor Kouznetsov
 Description: Tuesday Week 3 Notes, Tips and Tricks
'''

var = 12.34
var2 = 8
var3 = var/var2 #this is known as a "mixed expression"
print (var3)

var2=var2+3 #this our our updated statement
print(f'var2 is now {var2}')

#understand we have a compound operator (consists of a math operator followed by the = sign
var2+=3 #this statement is equivalent to var2 = var2 + (3)
print(f'var2 is now {var2}')


x = 5
y = 2
z = 2

#z = z * y + x
#print(f'z is now {z}')
z *= y + x #this statement is equivalent to z = z * (y+x)

z=z+y*z-x
print(f'z is now {z}')
z+=y*z-x
print(f'z is now {z}')

#z=z-x*z+y=2-5*2+2=2-10+2
#print(f'zis now {z}')
#z-=x*z+y #z=2-(5*2+2)
#print(f'z is now {z}')

#+=, -=, *=, /=, //=, %=, **=

#Formatting Options
#1: Use the format function
number = float(input('Enter a number: '))
print('The Number is', format(number, '.5f'))

#2: Use the string formatting with %
age = 9
print('My pet is %d years old' % age)
                              

#3: Use the format method
rate = 3.245
print('You get a {:.2f} rate'.format(rate))

amt, price = 12, 3.21
print('{}large eggs cost #{:.2f} at Publix'.format(amt,price))

#4: Use formatting within
mmjackpot = 800e6
print(f'The Megamillions jackpot is now $mmhackpot:,.4f')

#format percentages
discount = input()
discount(f'Discount: {discount:.2%}')
