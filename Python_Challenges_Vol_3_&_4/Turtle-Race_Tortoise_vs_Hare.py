'''
 Author: Connor Kouznetsov
 Description: My program is responsible for simluating a unique race between two types of turtles (Tortoise & Hare) using the turtle module.
'''

#ZebrasClubDiscountCode: 

#Begin setting up race by importing the turtle module and random 
import turtle
import random

#Format for the background screen when viewing the race
screen = turtle.Screen()
screen.title("Featured Turtle Race: Tortoise vs Hare")

#Calling draw_course and using "hideturtle()" functions, create the course 
def draw_course():
    setup_race_course = turtle.Turtle()
    setup_race_course.hideturtle()
    setup_race_course.penup()
    setup_race_course.setposition(-100, 100)
    setup_race_course.pendown()
    setup_race_course.setposition(-100, 100)

    setup_race_course.penup()
    setup_race_course.setposition(-100, 100)
    setup_race_course.pendown()
    setup_race_course.setposition(-100, 100)

draw_course()

#Create the Start and Finish Lines
start = turtle.Turtle()
start.penup()
start.goto(-100, 0)
start.pendown()
start.setposition(-100, 100)
start.write(f"START", font = ("Times New Roman", 15, "bold"), align = "left", move = False)
start.penup()
start.goto(125, 50)
start.color('black')

end = turtle.Turtle()
end.penup()
end.goto(100, 0)
end.pendown()
end.setposition(100, 100)
end.write(f"FINISH", font = ("Times New Roman", 15, "bold"), align = "left", move = False)
end.penup()
end.goto(125, 50)
end.color('black')

#Create the two racing turtles
Tortoise = turtle.Turtle(shape="turtle")
Tortoise.shapesize(2, 2)
Tortoise.speed(0)
Tortoise.penup()
Tortoise.setposition(-100, 25)

Hare = turtle.Turtle(shape="circle")
Hare.shapesize(1, 2)
Hare.speed(0)
Hare.penup()
Hare.setposition(-100, 75)

#Create the heading to display in the viewer window
header = turtle.Turtle()
header.hideturtle()
header.penup()
header.setposition(0, 180)
header.write(f"On Your Mark... Get Set... GO!", font = ("Times New Roman", 25, "bold"), align = "center")
header.goto(0, 150)
header.write(f"And They're Off!!!", font = ("Times New Roman", 25, "bold"), align = "center")

#Use the following define function to track the tortoise's movement...
def move_tortoise(current_pos):
    move_type = random.randint(1, 10)
    if 1 <= move_type <= 5: #Fast Plod: 50% Probability to move '3 Spaces Forward'
        current_pos += 3
    elif 6 <= move_type <= 7: #Slip: 20% Probability to move '5 Spaces Backward'
        current_pos -= 5
    else: #Slow Plod: 30% Probability to move '1 Space Foward'
        current_pos += 1

    #Boundary positioning for tortoise movement over the specified bounds (reset)
    if current_pos > 100:
        current_pos = 100
    elif current_pos < -100:
        current_pos = -100
    
    return current_pos

#Use the following define function to track the hare's movement...
def move_hare(current_pos):
    move_type = random.randint(1, 10)
    if 1 <= move_type <= 2: #Sleep: 20% Probability to move 'No Movement'
        current_pos += 0
    elif 3 <= move_type <= 4: #Big Hop: 20% Probability to move '7 Spaces Forward'
        current_pos += 7
    elif move_type == 5: #Big Slip: 10% Probability to move '10 Spaces Backward'
        current_pos -= 10
    elif 6 <= move_type <= 8: #Small Hop: 30% Probability to move '1 Space Forward'
        current_pos += 1
    else: #Small Slip: 20% Probability to move '2 Spaces Backward'
        current_pos -= 2
    
    #Boundary positioning for hare movement over the specified bounds (reset)
    if current_pos > 100:
        current_pos = 100
    elif current_pos < -100:
        current_pos = -100
    
    return current_pos

#State starting x position of racers
pos_of_tortoise = -100
pos_of_hare = -100
race_timer = 0

#Use while loop to simulate the program
while pos_of_tortoise < 100 and pos_of_hare < 100:
    race_timer += 1

    pos_of_tortoise = move_tortoise(pos_of_tortoise)
    pos_of_hare = move_hare(pos_of_hare)

    Tortoise.setposition(pos_of_tortoise, 25)
    Hare.setposition(pos_of_hare, 75)

    turtle.delay(50)

#Using an if/else statement to simulate the potential winner
if pos_of_tortoise >= 100 and pos_of_hare >= 100:
    if pos_of_tortoise >= pos_of_hare:
        Winner = "Tortoise"
    else:
        Winner = "Hare"
elif pos_of_tortoise >= 100:
    Winner = "Tortoise"
else:
    Winner = "Hare"

#Now Display the winner from the previous set of code
winner_result = turtle.Turtle()
winner_result.hideturtle()
winner_result.penup()
winner_result.goto(135, 42.5)
winner_result.write(f"{Winner} wins!", font = ("Times New Roman", 12, "bold"), align = "left",)
winner_result.goto(0, -60)
winner_result.write(f"{Winner} won the race in a total of {race_timer} 'seconds'.", font = ("Times New Roman", 15, "bold"), align = "center")

turtle.done()