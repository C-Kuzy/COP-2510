"""
 Author: Connor Kouznetsov
 Description: This is a python practice file for ZyLab's Under Activity #2
"""

'''*****ZyLab 2.15 Divide Input Integers*****'''

#Write a program that reads integers user_num and div_num as input, and outputs user_num divided by div_num three times using floor divisions.

'''If the input is user_num = 2000 & div_num = 2'''

#The Output must be printed as follows: "1000, 500, 250"
'''
import math

user_num = int(input())
div_num = int(input())

#use this information to output 1000, 500, and 250

total_aftr_div1 = (user_num // div_num)
remaining_num = total_aftr_div1
total_aftr_div2 = (remaining_num // div_num)
remaining_num2 = total_aftr_div2
total_aftr_div3 = (remaining_num2 // div_num)

#Now create the ouput as per the requirement above^^^

print(f"{total_aftr_div1} {total_aftr_div2} {total_aftr_div3}")
'''

'''*****Zylab 2.19 Using Math Functions*****'''

# Given three floating-point numbers x, y, and z, output x to the power of z, x to the power of (y to the power of z),
# the absolute value of (x minus y), and the square root of (x to the power of z).

# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f} {your_value4:.2f}')

'''If the input is 5.0 1.5 & 3.2''' #ASSUME THIS IS X, Y, Z

#The Output must be printed as follows: "172.47 361.66 3.50, 13.13"
'''
import math

#Create necessary inputs for 
x = float(input())
y = float(input())
z = float(input())

#Creating Necessary Statements given by the question
#output x to the power of z
your_value1 = (math.pow(x, z))

#x to the power of (y to the power of z)
your_value2 = (math.pow(x, (math.pow(y, z))))

#the absolute value of (x minus y)
your_value3 = (math.fabs(x - y))

#square root of (x to the power of z)
your_value4 = (math.sqrt(math.pow(x, z)))

print(f"{your_value1:.2f} {your_value2:.2f} {your_value3:.2f} {your_value4:.2f}")
'''

'''*****Zylab 2.20 Musical Note Frequencies*****'''

# On a piano, a key has a frequency, say f0. Each higher key (black or white) has a frequency of f0 * rn, where 
# n is the distance (number of keys) from that key, and r is 2(1/12). Given an initial key frequency, output that 
# frequency and the next 3 higher key frequencies.

# Output each floating-point value with two digits after the decimal point, then the units ("Hz"), then a newline
'''
import math

#Create necessary statements given by the question
f0 = float(input()) 

r = math.pow(2.0, (1/12))

your_value1 = (f0)
your_value2 = (your_value1 * r)
your_value3 = (your_value2 * r)
your_value4 = (your_value3 * r)

print(f"{your_value1:.2f} Hz\n{your_value2:.2f} Hz\n{your_value3:.2f} Hz\n{your_value4:.2f} Hz")
'''

deez_nutz = input()
how_are_u = input()

total = deez_nutz + how_are_u

print(total)