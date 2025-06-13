'''
 Author: Connor Kouznetsov
 Description: Week 6 Lecture 2 Oct 3rd
'''

for i in range (0, 10, 2): #remember that the range function is exclusive of the last number
    print(i)

#For a loop with a tuple
tuplex = (1, 2, 20, 500, 7)
for j in tuplex:
    print(f"{j}")

print()
#For a loop with a list
names = ['Connor', 'John', 'Jane', 'Doe']
for j in names:
    print(f"This is: {j}")

print()
#For a loop with a string
plan = 'I am going to the store'
for j in plan:
    print(f"{j}")

print()
#For a loop with a set
fish = ['salmon', 'tuna', 'mackerel', 'salmon', 'tuna', 'mackerel']
for i in set(fish):
    print(f"{i}")

print()
#For a loop with a dictionary
categories = {'name': 'Connor', 'age': 21, 'major': 'Computer Science'}
for i in categories:
    print(f"{i}: {categories[i]}") #This will print the key and the value
    print(f"{categories[i]}") #This will only print the value

#For a loop with the range function
for b in range (len(names)):
    print(f"Hi {names[b]}!") 

names = ["Connor", "John", "Jane", "Doe", 10, 100]

for i, j in enumerate(names):
    print(f"{i}.....{j}")

print()


import random
for k in range (1, 6):
    print(random.randint(1, 6)) #includes the upper limit

print()
for j in range (10, 5, -1): # Starting: 10, Ending: 5, Step: -1
    print(random.randrange(1, 6)) #This excludes the upper limit

print()
for m in range(5):
    print(random.uniform(3.5, 4.0)) #Upper limit may be included

print()
for m in range(5):
    print(random.random() * 60) #Float values from 0-1

deck = ["Spades", "Hearts", "Clubs", "Diamonds", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
for m in range(5):
    print(random.choice(deck))

while True: #Given an infinite loop
    print("There's an infinite loop")
    break #Interrupt the for loop
    
i = 1
while True:
    print("Hello!")
    i = i + 1
    if i > 6:
        break

while i < 12:
    print("Better!")
    i += 1

for LCV in range(1, 21):
    if LCV == 5 or LCV == 15:
        continue #This skips an iteration but allows the loop to continue

    print(f"{LCV}", end = " ") #This will print the numbers 1-20 except for 5 and 15

for i in range(1, 11):
    if i == 7:
        break
    
    print(i)
else:
    print("We have successfully completed the loop")

for i in range(1, 7):
    for j in range(1, 7):
        print(f"{i} {j}")

digit = 0
while digit <= 9: #outer loop
    dig2 = 0
    break #Outer loop was interrupted before the inner loop
    while dig2 <= 9: #inner loop
        print(f"{digit} -- {dig2}")
        dig2 += 1
        break #Inner loop was interrupted before the outer loop
    else:
        print("This is awesome")

    digit += 1


import turtle
turtle.shape("turtle") #This changes the cursor to a turtle
                        #Also allowed: 'triangle', 'arrow', 'classic', 'square', 'circle'

turtle.pendown()
turtle.speed(1) #This sets the speed of the cursor to 1
                #Removes as much time as possible between the movements of the cursor

for i in range(4):
    turtle.speed(0)
    turtle.backward(100) #This mves the cursor foward 100 pixels
    turtle.dot(10, 'blue') #This places a dot of the color blue
    turtle.left(90) #This rotates the cursor 90 degrees to the left

turtle.clearscreen() #This clears the screen aka the drawing board

for i in range (3):
    turtle.speed(0)
    turtle.backward(100) #This moves the cursor backward 100 pixels
    turtle.dot(10, 'blue') #This places a dot of the color blue
    turtle.left(120) #This rotates the cursor 120 degrees to the left

turtle.clearscreen() #This clears the screen aka the drawing board
turtle.speed(0)
for i in range(10):
    turtle.circle(75) #This creates a circle with a radius of 75 pixels
    turtle.rt(36) #This rotates the cursor 36 degrees to the right