'''
 Author: Connor Kouznetsov
 Description: This program focuses on assisting the user in selecting a resturant based on their friend's potential dietary restrictions.
'''

resturants = {
    "Council Oak Steaks & Seafood": {"Vegetarian": False, "Vegan": False, "Gluten_Free": False},
    "Wood Fired Pizza Wine Bar": {"Vegetarian": True, "Vegan": False, "Gluten_Free": True},
    "Villaggio's Ristorante Italiano": {"Vegetarian": True, "Vegan": False, "Gluten_Free": False},
    "Faramcy Vegan Kitchen": {"Vegetarian": True, "Vegan": True, "Gluten_Free": True}
}

#Create necessary input functions for the user to input their preferences
Vegetarian = input("Is anyone in your party a vegetarian? (yes/no) ").lower().strip()
Vegan = input("Is anyone in your party a vegan? (yes/no) ").lower().strip()
Gluten_Free = input("Is anyone in your party gluten-free? (yes/no) ").lower().strip()

#The use of .lower() will convert the user's input(s) to lowercase
#The use of .strip() will remove any leading or trailing white spaces from the user's input

#Create a list that will store the resturants that are suitable for the user's dietary restrictions
suitable_resturants = ["Council Oak Steaks & Seafood", "Wood Fired Pizza Wine Bar", "Villaggio's Ristorante Italiano", "Faramcy Vegan Kitchen"]

#Cycle through the dictonary to determine which resturants are suitable for the user's party
for resturant, restrictions in resturants.items():
    if Vegan == "yes" and restrictions["Vegan"] == False:
        suitable_resturants.remove(resturant)
    elif Vegetarian == "yes" and restrictions["Vegetarian"] == False and restrictions["Vegan"] == False:
        suitable_resturants.remove(resturant)
    elif Gluten_Free == "yes" and restrictions["Gluten_Free"] == False:
        suitable_resturants.remove(resturant)

#The use of elif will allow the program to check the next condition if the previous condition is false.

#Now print out the resturants that are suitable for the user's party of friends
print("Here are your resturant choices:")
for resturant in suitable_resturants:
    print(resturant)