'''
 Author: Connor Kouznetsov
 Description: This test Calculates the lenth of a runway a plane needs to takeoff
'''

#Step 1: List and classify necessary varaibles
Take_Off_Speed = float(input("Enter the plane's take off speed in m/s: "))
Acceleration = float(input("Enter the plane's acceleration in m/s**2: "))

#Step 2: Use necessary calculations to determine the minimum length of the runway
Length_Of_Runway = (Take_Off_Speed ** 2) / (2 * Acceleration)

#the use of "**" represents a squared value to substitute for (v^2)
#the problem states that the formula is (v ** 2 / 2 * a)

#Step 3: Display the output of the runway length
print('The minimum runway length needed for this airplane to takeoff is', f'{Length_Of_Runway:.4f}', 'meters.')

#End of program, make sure to save, then run to test results!!!
