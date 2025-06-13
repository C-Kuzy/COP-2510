"""
Author: Connor Kouznetsov
"""

#PROGRAM #1 - Calculate the number of calories burned

''' Calories = ((Age x 0.2757) + (Weight x 0.03295) + (Heart Rate x 1.0781) — 75.4991) x Time / 8.368 '''

''' Type your code here. '''

#Variable Input for equation specification
Age = float(input())
Weight = float(input())
Heart_Rate = float(input())
Time = float(input())

#Now make basic equations to simplify code in the f string print line...
Age = (Age * 0.2757)
Weight = (Weight * 0.03295)
Heart_Rate = ((Heart_Rate * 1.0781) - 75.4991)
Time = Time

Calories = (((Age + Weight + Heart_Rate) * Time)/ 8.368)
print(f'Calories: {Calories:.2f} calories')

#PROGRAM #2 - Calculate the amount of Pizza's needed for a party

''' Pizza = (People x Slices per person) / Slices per pizza '''

People = int(input())
Slices_Per_Person = int(input())
