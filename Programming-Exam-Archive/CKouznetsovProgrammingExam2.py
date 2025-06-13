"""
 Name: Connor Kouzentsov
 Description: Building an information entrance system for 
             an animal shelter that contains cats and dogs
"""
#Part 1: Ensure the information above is correct and describes the program

#Part 2: Create the parent class: "Animal"

class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Species: {self.species}"

class Dog(Animal):
    def __init__(self, name, age, species, dog_breed):
        Animal.__init__(self, name, age, species)
        self.dog_breed = dog_breed

    def __str__(self):
        Animal.__str__(self)
        return f"Name: {self.name}, Age: {self.age}, Species: {self.species}, Breed: {self.dog_breed}"


class Cat(Animal):
    def __init__(self, name, age, species, cat_type):
        Animal.__init__(self, name, age, species)
        self.cat_type = cat_type
        
    def __str__(self):
        Animal.__str__(self)
        return f"Name: {self.name}, Age: {self.age}, Species: {self.species}, Type: {self.cat_type}"

"--------------------------------------End of Classes--------------------------------------------"

#Step 7: Extra Credit, create function called "filterbyspecies" and create necessary parameters

def filter_by_species(opt, an_list): #"opt" was submitted as "choice" since we can correlate choice as options.
    match opt.lower():
        case "dog":
            print("Searching our system for dogs... ... ...")
            for animals in an_list:
                if animals.species.lower() == "dog":
                    print(animals)
        case _: #underscore used as this is shuffles the case for cat which is different than dog
            print("Searching out system for cats... ... ...")
            for animals in an_list:
                if animals.species.lower() == "cat":
                    print(animals)            
                    
# Step 4: Create Necessary Functions to properly add, search, choose, and display the entered animal list

def add_animals(num_animals):
    animal_list = []
    for animals in range(num_animals):
            animal_type = input("\nAnimal species: ")
            
            if animal_type.lower() == "dog":
                name = input("Animal name: ")
                age = input("Animal age: ")
                breed = input("Type of dog: ")
                animal = Dog(name, age, animal_type, breed)

            elif animal_type.lower() == "cat":
                name = input("Animal name: ")
                age = input("Animal age: ")
                cat_type = input("Indoor or Outdoor cat? ")
                animal = Cat(name, age, animal_type,  cat_type)
            animal_list.append(animal)

    return animal_list

# Step 5: As part of the driver, create function called "display__animals" (works with Step 4)

def display_animals(an_list):
    print("\nThe following animals have successfully been added to our shelter:")
    for animals in an_list:
        print(animals)

# Step 6: Ensure that the program prompts the user for both num of animals and functions to call pt 4/pt 5    

def main_funct():
    print("Welcome to the Greater Area USF Animal Shelter")
    num_animals = int(input("How many Animals (Dog(s) and/or Cat(s)) are being added to our system?: "))
    animal_list = add_animals(num_animals)
    display_animals(animal_list)

    #v Also in Part 7: Extra Credit, Step 2 v

    opt1 = input("\nAre you searching for a specific species? Enter 'yes' or 'no' ")
    match opt1:
        case 'yes':
            opt2 = input("Would you like to filter by Dog or Cat? ")
            filter_by_species(opt2, animal_list)

        case _: #The underscore represents an input if something other than "yes" is said
            print("Thank you for visiting the Greater Area USF Animal Shelter! Hope you visit again soon!")
            

"--------------------------------------End of Functions--------------------------------------------"

#FIAL STEP: Test the function by calling it
main_funct()

