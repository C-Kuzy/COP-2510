'''
 Author: Connor Kouznetsov
 Description: Using Math Functions
'''

#Given three floating-point numbers x, y, and z, output x to the power of z, x to the power of 
#(y to the power of z), and the absolute value of x minus y, and the square root of x to the power of z.
'''
Ex: If the input is:
Input_1 = 5.0
Input_2 = 1.5
Input_3 = 3.2

Then the output is:
172.47, 361.66, 3.50, 13.13
'''

import math

x = float(input())
y = float(input())
z = float(input())

your_value1 = x ** z #or sub for x_power_z
your_value2 = x ** (y ** z) #or sub for x_power_y_power_z
your_value3 = abs(x - y) #or sub for absolute_difference
your_value4 = math.sqrt(x ** z) #or sub for square_root_x_power_z

print(f"{your_value1:.2f} {your_value2:.2f} {your_value3:.2f} {your_value4:.2f}")

#Program Completed Successfully :D