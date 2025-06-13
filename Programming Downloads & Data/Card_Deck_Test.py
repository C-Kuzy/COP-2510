# import random
# suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
# ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
# deck = []

# for suit in suits:
#     for rank in ranks:
#         card = (f"{rank} of {suit}")
#         deck.append(card)
# while len(deck) > 0:
#     input("Press Enter to draw a card from the deck")
#     user_card = deck[random.randint(0, len(deck) - 1)]
#     deck.remove(user_card)
#     print(user_card)

import turtle
for i in range (360):
    turtle.shape("turtle")
    turtle.pendown()
    turtle.speed(100)
    turtle.circle(75)
    turtle.rt(0.5)
turtle.done()