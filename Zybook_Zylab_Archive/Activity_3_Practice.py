"""
 Author: Connor Kouznetsov
 Description: This is a python practice file for ZyLab's under Activity #3
"""

'''*****ZyLab 3.14 Input and formatted output: Caffine levels*****'''

#A half-life is the amount of time it takes for a substance or entity to fall to half its original value.
#Caffeine has a half-life of about 6 hours in humans. Given an initial amount of caffeine, output the caffeine level after 6, 12, and 24 hours.
#Output each floating-point value with two digits after the decimal point

#Input = 100

#OUTPUT = 50.00 mg, 25.00 mg, 6.25 mg

caffeine_mg = float(input())
half_life_hours = 6
h_l_hr1 = int(input())
h_l_hr2 = int(input()) 
h_l_hr3 = int(input())

#From the code above, we know that our caffeine variable is in mg or milligrams'
#We can also notice that the half life variable is assigned to the input of hours
#ALSO ensure that we use print(f"{your_value:.2f}") to output the float with 2 decimal points 

#Create equation necessary for solving the total amount of mg left after x hours
h_l_eq1 = caffeine_mg*(1/2)**(h_l_hr1/half_life_hours) 
h_l_eq2 = caffeine_mg*(1/2)**(h_l_hr2/half_life_hours)
h_l_eq3 = caffeine_mg*(1/2)**(h_l_hr3/half_life_hours)

#Now we need to create f string statements that will allow us to create the output
print(f"After {h_l_hr1} hours: {h_l_eq1:.2f} mg"); print(f"After {h_l_hr2} hours: {h_l_eq2:.2f} mg"); print(f"After {h_l_hr3} hours: {h_l_eq3:.2f} mg")