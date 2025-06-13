"""
Author: Connor Kouznetsov
Description: E2 Practice
"""

#Example #1: Creating a Store recieving inventory by using Classes, Def, Initizlig, Sorting, and Searching methods
'''
class StoreItem:
    """Represents an item in the store."""
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}, Quantity: {self.quantity}"

class StoreInventory:
    """Manages store items with sorting and searching functionality."""
    def __init__(self):
        self.items = []

    def add_item(self, name: str, price: float, quantity: int):
        """Adds a new item to the inventory."""
        new_item = StoreItem(name, price, quantity)
        self.items.append(new_item)
    
    def display_items(self):
        """Displays all items in the inventory."""
        for item in self.items:
            print(item)

    def sort_items(self, key: str):
        """Sorts items based on the specified attribute: 'name', 'price', or 'quantity'."""
        if key == "name":
            self.items.sort(key=lambda item: item.name.lower())
        elif key == "price":
            self.items.sort(key=lambda item: item.price)
        elif key == "quantity":
            self.items.sort(key=lambda item: item.quantity)
        else:
            print("Invalid sorting key. Choose 'name', 'price', or 'quantity'.")

    def search_item(self, name: str):
        """Searches for an item by name."""
        results = [item for item in self.items if name.lower() in item.name.lower()]
        return results if results else "No items found."

# Example usage:
inventory = StoreInventory()

# Adding items
inventory.add_item("Laptop", 999.99, 5)
inventory.add_item("Headphones", 49.99, 15)
inventory.add_item("Keyboard", 89.99, 10)

# Sorting items by price
inventory.sort_items("price")
inventory.display_items()

# Searching for an item
search_results = inventory.search_item("Laptop")
print("\nSearch Results:")
for item in search_results:
    print(item)
''''''
#Example #2: An animal shelter that    

class Animal:
    # This class grants the ability to add animals to our shelter list based on specifics.
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Species: {self.species}"


class Dog(Animal):
    def __init__(self, name, age, species, breed):
        super().__init__(name, age, species)
        self.breed = breed

    def __str__(self):
        # Leverage the parent's __str__ method to avoid repetition.
        return f"{super().__str__()}, Breed: {self.breed}"


class Cat(Animal):
    def __init__(self, name, age, species, cat_type):
        super().__init__(name, age, species)
        self.cat_type = cat_type

    def __str__(self):
        # Use the parent's __str__ method and then add cat-specific info.
        return f"{super().__str__()}, Type: {self.cat_type}"

'''
# --- End of Classes ----
'''
def add_animals(num_animals):
    animal_list = []
    for _ in range(num_animals):
        animal_type = input("\nAnimal species (dog/cat): ").strip().lower()
        
        if animal_type == 'dog':
            name = input("Animal name: ")
            age = input("Animal age: ")
            breed = input("Type of Dog: ")
            animal = Dog(name, age, animal_type, breed)
        
        elif animal_type == 'cat':
            name = input("Animal name: ")
            age = input("Animal age: ")
            cat_type = input("Indoor or Outdoor Cat? ")
            animal = Cat(name, age, animal_type, cat_type)
        
        else:
            print("Invalid animal species. Please enter either 'dog' or 'cat'.")
            continue  # Skip adding if not recognized.
        
        animal_list.append(animal)

    return animal_list


def display_animals(an_list):
    print("\nHere are the animals added to the shelter:")
    for animal in an_list:
        print(animal)


def species_filter(choice, an_list):
    # Ensure the filter check is case-insensitive.
    filter_choice = choice.strip().lower()
    if filter_choice == "Dog":
        print("Searching for all Dogs...\n(-*40)")
        for animal in an_list:
            if animal.species.lower() == "Dog":
                print(animal)
    elif filter_choice == "cat":
        print("Searching for all cats...")
        for animal in an_list:
            if animal.species.lower() == "Cat":
                print(animal)
    else:
        print("Sorry, that species is not recognized.")


def primary_funct():
    print("Welcome to the University of South Florida Animal Shelter!")
    num_animals = int(input("How many animals will be added to the shelter: "))
    animal_list = add_animals(num_animals)
    display_animals(animal_list)

    opt_num1 = input("\nIs there a specific animal species you're looking for today? Enter 'YES' or 'NO': ").strip().lower()
    if opt_num1 == "yes":
        opt_num2 = input('Filter by dog or cat? ').strip().lower()
        species_filter(opt_num2, animal_list)
    else:
        print('No worries, maybe next time.')


# --- End of Functions ----

# Solidify the primary function call.
primary_funct()

'''



