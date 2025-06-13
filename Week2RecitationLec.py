"""
 Name: Connor Kouznetsov
 Description: Friday Afternoon Recitation Drawing Tutorial
"""

import turtle

#Draw a Triangle
'''turtle.pendown()
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.penup()'''

'''
#Draw a Pentagon
turtle.pendown()
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.penup()
turtle.done()
'''

'''
#Draw a Square
turtle.pendown()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.penup()
turtle.done()


while True:
    turtle.done() #Keeps the turtle window open
    pass '''

import turtle
import random

# Function to track the tortoise's movement
def move_tortoise(current_pos):
    move_type = random.randint(1, 10)
    if move_type <= 5:  # Fast Plod: 50% Probability to move '3 Spaces Forward'
        new_pos = current_pos + 3
    elif move_type <= 7:  # Slip: 20% Probability to move '5 Spaces Backward'
        new_pos = current_pos - 5
    else:  # Slow Plod: 30% Probability to move '1 Space Forward'
        new_pos = current_pos + 1

    # Boundary positioning for tortoise movement
    if new_pos < -100:
        new_pos = -100
    elif new_pos > 100:
        new_pos = 100
    return new_pos

# Function to track the hare's movement
def move_hare(current_pos):
    move_type = random.randint(1, 10)
    if move_type <= 2:  # Sleep: 20% Probability to move 'No Movement'
        new_pos = current_pos + 0
    elif move_type <= 4:  # Big Hop: 20% Probability to move '7 Spaces Forward'
        new_pos = current_pos + 7
    elif move_type <= 5:  # Big Slip: 10% Probability to move '10 Spaces Backward'
        new_pos = current_pos - 10
    elif move_type <= 8:  # Small Hop: 30% Probability to move '1 Space Forward'
        new_pos = current_pos + 1
    else:  # Small Slip: 20% Probability to move '2 Spaces Backward'
        new_pos = current_pos - 2

    # Boundary positioning for hare movement
    if new_pos < -100:
        new_pos = -100
    elif new_pos > 100:
        new_pos = 100
    return new_pos

# Setup the race screen
screen = turtle.Screen()
screen.title("Featured Turtle Race: Tortoise vs Hare")
screen.bgcolor("lightgrey")

# Create turtles for the race
Tortoise = turtle.Turtle()
Hare = turtle.Turtle()

Tortoise.shape("turtle")
Tortoise.shapesize(2, 2)
Tortoise.color("green")
Tortoise.penup()
Tortoise.setpos(-100, 50)
Tortoise.pendown()

Hare.shape("triangle")
Hare.shapesize(2, 2)
Hare.color("brown")
Hare.penup()
Hare.setpos(-100, 0)
Hare.pendown()

# Draw the race course
course_drawer = turtle.Turtle()
course_drawer.hideturtle()
course_drawer.penup()
course_drawer.setpos(-200, 100)
course_drawer.pendown()
course_drawer.angle(90)
course_drawer.forward(200)  # Draw starting line
course_drawer.penup()
course_drawer.setpos(-200, -100)
course_drawer.pendown()
course_drawer.angle(90)
course_drawer.forward(200)  # Draw finish line

# Race tracking variables
tortoise_position = -100
hare_position = -100
race_clock = 0

# Main race loop
while tortoise_position < 100 and hare_position < 100:
    race_clock += 1
    
    # Update positions
    tortoise_position = move_tortoise(tortoise_position)
    hare_position = move_hare(hare_position)

    # Move turtles on the screen
    Tortoise.setpos(tortoise_position, 50)
    Hare.setpos(hare_position, 0)

# Determine the winner
if tortoise_position >= hare_position:
    winner = "Tortoise wins!"
else:
    winner = "Hare wins!"

# Display the result
result_turtle = turtle.Turtle()
result_turtle.hideturtle()
result_turtle.penup()
result_turtle.setpos(0, -250)
result_turtle.write(f"{winner}\nRace took {race_clock} iterations!", align="center", font=("Arial", 24, "bold"))

# End the race
turtle.done()
