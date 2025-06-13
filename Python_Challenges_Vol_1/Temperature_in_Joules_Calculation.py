'''
 Author: Connor Kouznetsov
 Description: Calculating Water Temperature in Joules
'''

#Step 1: Create/Set Necessary Variables for the program 
Water_Weight = float(input('Enter the amount of water (in kg): '))
Initial_Temperature = float(input('Enter the initial temperature of the water (Celsius): '))
Final_Temperature = float(input('Enter the final temperature of the water (Celsius): '))

#Step 2: Using provided data, define necessary items for the equation: Q = M * (FT - IT) * 4184
Temperature_Difference = (Final_Temperature - Initial_Temperature)
Constant = 4184

#Step 3: Create a equation that will evaluate the one stated in Step 2...
Energy_Joules = Water_Weight * Temperature_Difference * Constant

#Step 4: Use the previous steps to create a statement that displays our required energy in joules.
print('The energy required to heat the water is', f'{Energy_Joules:,.1f}', 'Joules.')

#End of program, make sure to save, then run to test results!!!

