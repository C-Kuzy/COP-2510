'''
 Author: Connor Kouznetsov
 Description: This exercise focuses on calculating the total shaded area of the composite shape
'''

import math

#Step 1: Create/List necesssary variables
Diagonal_Length_X = float(input('Enter the first diagonal length: '))
Diagonal_Length_Y = float(input('Enter the second diagonal length: '))
Radius_Length = float(input('Enter the radius of the enclosed circle: '))

#Step 2: Using the information provided, define necessary items for the area equation
Total_Area_Shape = (Diagonal_Length_X * Diagonal_Length_Y) / 2

#Step 3: Make sure that the value Pi is defined in our program
Pi = 3.14159
Area_Circle = Pi * (Radius_Length ** 2)

#Step 4: Using the information provided, create an equation to solve for the shaded region
Total_Shaded_Area = Total_Area_Shape - Area_Circle

#Step 4: Use the previous steps to display the total shaded area of the composite shape
print('The shaded area of our composite shape is', f'{Total_Shaded_Area:.3f}', 'square units.')

#End of program, make sure to save, then run to test results!!!
