'''
 Author: Connor Kouznetsov
 Description: This test focuses on Value Swapping two variables
'''

#Step 1: Begin by classifying variable input(s)
Integer_X = input('Please enter your first integer')
Integer_Y = input('Please enter your second integer')

#Step 2: Write a statement to check the values before the swap
print(f'Before the number swap, Integer_X and Integer_Y are: ')

#Step 3: Display the output(s) prior to the number swap
print(f'Integer_X = {Integer_X}, and Integer_Y = {Integer_Y}')

#Step 4: Write a statement to check the values after the swap
print(f'After the number swap, Integer_X and Integer_Y are: ')

#Step 5: Perform the Number Swap with the following...
Integer_X, Integer_Y = Integer_Y, Integer_X

#Step 6: Display the output(s) following the number swap
print(f'Integer_X = {Integer_X}, Integer_Y = {Integer_Y}')

#End of program, make sure to save, then run to test results!!!
