'''
 Author: Connor Kouznetsov
 Description: This program simulates a makeshift version of the game: "The Price is Right" 
              that you can play with your friends and acquaintances.
'''

#Import the random and randint modules to deal with random number generation 
import random
from random import randint

#Generate a random number for the price of the price (set the range from $1000 to $5000)
price = random.randint(1000, 5000)
print(price)

#Create necessary input functions for the user to have a profile to input their bids
player_1 = int(input("Player 1, what is your bid? "))
player_2 = int(input("Player 2, what is your bid? "))   
player_3 = int(input("Player 3, what is your bid? "))
player_4 = int(input("Player 4, what is your bid? "))

#Create a statement The use of if statements will determine the outcome of the game
#The use of elif statements will allow the program to check the next condition if the previous condition is false.
if player_1 == price:
    print("Ding Ding Ding! One player got it exactly right and gets $500!") 
    print(f"Actual price is ${price}! Player 1, come on up!")
elif player_2 == price:
    print("Ding Ding Ding! One player got it exactly right and gets $500!")
    print(f"Actual price is ${price}! Player 2, come on up!")
elif player_3 == price:
    print("Ding Ding Ding! One player got it exactly right and gets $500!") 
    print(f"Actual price is ${price}! Player 3, come on up!")
elif player_4 == price:
    print("Ding Ding Ding! One player got it exactly right and gets $500!")
    print(f"Actual price is ${price}! Player 4, come on up!")

#Situation 1, if all players overbid the price then...
if player_1 > price and player_2 > price and player_3 > price and player_4 > price:
    print("Buzz! Awww... everyone has overbid!")

#FOR THE 4 PLAYERS, THERE ARE MULTIPLE SCENARIOS THAT CAN OCCUR FOR EACH PLAYER
#The use of comparison operators will allow the program to compare the player's bid to the actual price
#Now, in order to determine player 1's bid, we can use the following 'if' and 'elif' statements
#This is one way to determine player 1's bid
if player_1<price and player_1 > player_2 and player_1>player_3 and player_1>player_4:
    print(f'Actual price is ${price}! Player 1 come on up')
elif player_2 > price:
    print(f"Actual price is ${price}! Player 1 come on up")
elif player_3 > price:
    print(f"Actual price is ${price}! Player 1 come on up")
elif player_4 > price:
    print(f"Actual price is ${price}! Player 1 come on up")

#Now, in order to determine player 2's bid, we can use the following 'if' and 'elif' statements
if player_2<price and player_2 > player_1 and player_2>player_3 and player_2>player_4:
    print(f'Actual price is ${price}! Player 2 come on up')
elif player_2<price and player_2 > player_1 and player_2>player_3 and player_2<price<player_4:
    print(f'Actual price is ${price}! Player 2 come on up')
elif player_2<price and player_2 > player_1 and player_2<price<player_3 and player_2>player_4:
    print(f'Actual price is ${price}! Player 2 come on up')
elif player_2<price and player_2 > player_1 and player_2<price<player_3 and player_2<price<player_4:
    print(f'Actual price is ${price}! Player 2 come on up')
elif player_2<price and player_2<price<player_1 and player_2>player_3 and player_2<price<player_4:
    print(f'Actual price is ${price}! Player 2 come on up')
elif player_2<price and player_2<price<player_1 and player_2>player_3 and player_2>player_4:
    print(f'Actual price is ${price}! Player 2 come on up')
elif player_2<price and player_2<price<player_1 and player_2<price<player_3 and player_2<price<player_4:
    print(f'Actual price is ${price}! Player 2 come on up')
elif player_2<price and player_2<price<player_1 and player_2<price<player_3 and player_2>player_4:
    print(f'Actual price is ${price}! Player 2 come on up')

#Now, in order to determine player 3's bid, we can use the following 'if' and 'elif' statements
#Another way to determine player 3's bid is to use the following 'if' and 'elif' statements
if player_3<price and player_3 > player_2 and player_3>player_1 and player_3>player_4:
    print(f'Actual price is ${price}! Player 3 come on up')
elif player_1 > price:
    print(f"Actual price is ${price}! Player 3 come on up")
elif player_2 > price:
    print(f"Actual price is ${price}! Player 3 come on up")
elif player_4 > price:
    print(f"Actual price is ${price}! Player 3 come on up")

#Now, in order to determine player 4's bid, we can use the following 'if' and 'elif' statements
#We can consider this code to be the indepth way to determine player 4's bid
if player_4<price and player_4 > player_2 and player_4>player_3 and player_4>player_1:
    print(f'Actual price is ${price}! Player 4 come on up')
elif player_4<price and player_4 > player_2 and player_4>player_3 and player_4<price<player_1:
    print(f'Actual price is ${price}! Player 4 come on up')
elif player_4<price and player_4 > player_2 and player_4<price<player_3 and player_4>player_1:
    print(f'Actual price is ${price}! Player 4 come on up')
elif player_4<price and player_4 > player_2 and player_4<price<player_3 and player_4<price<player_1:
    print(f'Actual price is ${price}! Player 4 come on up')
elif player_4<price and player_4<price<player_2 and player_4>player_3 and player_4<price<player_1:
    print(f'Actual price is ${price}! Player 4 come on up')
elif player_4<price and player_4<price<player_2 and player_4>player_3 and player_4>player_1:
    print(f'Actual price is ${price}! Player 4 come on up')
elif player_4<price and player_4<price<player_2 and player_4<price<player_3 and player_4<price<player_1:
    print(f'Actual price is ${price}! Player 4 come on up')
elif player_4<price and player_4<price<player_2 and player_4<price<player_3 and player_4>player_1:
    print(f'Actual price is ${price}! Player 4 come on up')

#After taking 2 hours trying to figure this out, sorry to anyone who has to read this haha. 
