"""
 Author: Connor Kouznetsov
 Description: This program focuses on creating an effective checkout system 
for a store that contains multiple electronic devices for sale.
"""

#Define the electronic catalog by using a dictonary
electronics_catalog = {
    "Laptop": {"Price": float(2000)},
    "Desktop": {"Price": float(1400)},
    "Tablet": {"Price": float(600)},
    "Phone": {"Price": float(1000)}
}

#Creating a function to display the catalog prices
def display_item_prices():
    print("\nAvailable Electronic Devices:")
    for electronic, details in electronics_catalog.items():
        print(f"{electronic}: ${details["Price"]:.2f} each")
    print()

#Creating a function that adds any chosen item to the cart 
def add_item_cart(electronic_name):
    item_cart = []
    if electronic_name in electronics_catalog:
        if electronics_catalog[electronic_name]["Price"] > 0:
            item_cart.append(electronics_catalog[electronic_name]["Price"])
            print(f"You have successfully added '{electronic_name}' to your cart!")
        else:
            print(f"Oops, '{electronic_name} is not currently available.")
    else:
        print(f"'{electronic_name} does not exist within the Electronic Store Catalog.")


#Create a function that is calculates the sum of the values within the cart
def cart_total(electronic_name):
    if total_price > 5000.00:
        discounted_price = (total_price * (-0.10))
        total_price -= discounted_price
        print(discounted_price)
        print(total_price)
    else:
        return total_price

#Main program loop
def Mn_Elec_SYS():
    while True:
        print("\nWelcome to the virtual Electronic Store System!")
        print("Please choose from one of the following options in Stock")
        print("\n1. Display all available electonics!")
        print("2. Add an Electronic to the Cart!")
        print("3. View your Cart!")
        print("4. Display Total Price!")
        print("5. Done")

        #Now the user needs an option to choose
        try:
            u_d = int(input("\nEnter your selection (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        #Create selection structure to compute our user's input...
        if u_d == 1:
            display_item_prices()
        elif u_d == 2:
            electronic_name = input("Enter the name of the electronic you want to add to your cart: ")
            add_item_cart(electronic_name)
        elif u_d == 3:
            if cart_total(electronic_name):
                continue
            else:
                print("Your cart is Empty.")
        elif u_d == 4:
            cart_total()
        elif u_d == 5:
            print("Thank you for stopping by and using the Electronic Store System! Hope to see you again soon")
            break
        else:
            print("Invalid selection. Please try again.")


#Finally, Run the Electronic Store System
Mn_Elec_SYS()