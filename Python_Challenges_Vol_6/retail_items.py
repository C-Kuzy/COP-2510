'''
 Author: Connor Kouznetsov
 Description: My program is responsible for displaying and calculating the price you will pay for certain items.
'''

import math

class RetailItem:
    def __init__(self, typeUnit, unitamount, value):
        self.__typeUnit = typeUnit
        self.__units = unitamount
        self.__price = value

    def __str__(self):
        return f"{self.__typeUnit:<20} {self.__units:<10} ${self.__price:>7.2f}"
    
def mainfunct():
    number_Of_Items = int(input("Please Enter the Amount of Items You Would Like to Purchase!: "))
    while number_Of_Items <= 0: 
        print("Not Valid! Please enter a number greater than 0.")

    myItems = []

    for w in range (number_Of_Items):
        try:
            typeUnit = input(f"Enter the Type of Unit {w + 1}: ")
            unitamount = int(input(f"Enter the Total Units {w + 1}: "))
            value = float(input(f"Enter the Price {w + 1}: "))
        except:
            w -= 1
            print("Not Valid! Please enter a valid integer or price.")
            continue
        print()
        myItems.append(RetailItem(typeUnit, unitamount, value))

    print("\nThis is a Summary of the Items you Would Like to Purchase: ")
    print(41 * "-")
    print(f"{'Type of Unit':<20} {'Units':<10} {'Price':>7}")
    print(41 * "-")
    for items in myItems:
        print(items)

if __name__ == "__main__":
    mainfunct()