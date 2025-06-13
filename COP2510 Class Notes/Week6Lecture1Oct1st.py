'''
 Author: Connor Kouznetsov
 Description: Week 6 Lecture 1 Notes
'''

#count is controlled while loops
i=1 #initializatio
while i<= 5: #while condition
    print(f'{i}') 
    i+=1 #increment update

#while loop for input validation (with walrus operator)
while(int(input('Enter a positive number')))<0:
    print('Invalid input')


#HURRICANE #1 STILL HITTING