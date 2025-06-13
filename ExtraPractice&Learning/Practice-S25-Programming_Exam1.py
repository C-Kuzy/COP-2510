"""
Author: Connor Kouznetsov
U-Number: ####
Description: This python file contains multiple practice examples that might be used for the exam
"""

""" Programming Exam #1 Topics: Dictionaries, Selection Structures or Expressions, Loops (While &/or For Loops), & Functions"""


#min() to find smallest value % max() to find the largest value
#.isdigit checks if all characters are digits
#.isupper() / .islower() checks if all characters excluding numbers is case sensitive
#try exceptValueError structure
#.strip removes whitespace besides between characters
#.capitalize capitalizes first character of string
#.split splits all characters separated by spaces creating an index
#.count can count number of instances of a character or phrase in a string
#.endswith ensures ending in specific method
#you can align with :</^/>10 

#break can only be used in while loops or if else with a while True:


#job = input()
#if job not in my_dict:
    #print('Invalid key')
    #job = input()
#my_dict['city'] = 'New York' to add to dictionary

#no need for while __ in dict: in if elif
#var = input().lower()
#can use while True: to create loop for value error

#.update({'job' : 'engineer', 'country : 'usa'})
#del my_dict['age']
#removed_value = my_dict.pop('job') removes job key and prints engineer
#key,  value = my_dict.popitem() remomves and returns last inserted key-value pair
#.clear removes all elements

#The purpose of .split() is to split a string into a list of substrings based on a delimiter. By default, the delimiter is a space character.
#The purpose of .strip() is to remove leading and trailing whitespace from a string.



'''Example #1''' #Creating a library scanning system...
# Define the library catalog using a dictionary
library_catalog = {
    "1984": {"author": "George Orwell", "copies_available": 3},
    "To Kill a Mockingbird": {"author": "Harper Lee", "copies_available": 2},
    "The Great Gatsby": {"author": "F. Scott Fitzgerald", "copies_available": 5},
    "Pride and Prejudice": {"author": "Jane Austen", "copies_available": 4}
}

# Function to display available books
def display_books():
    print("\nAvailable Books:")
    for book, details in library_catalog.items():
        print(f"{book} by {details['author']} - {details['copies_available']} copies available")
    print()

# Function to borrow a book
def borrow_book(book_name):
    if book_name in library_catalog:
        if library_catalog[book_name]["copies_available"] > 0:
            library_catalog[book_name]["copies_available"] -= 1
            print(f"You have borrowed '{book_name}'. Enjoy reading!")
        else:
            print(f"Sorry, '{book_name}' is currently unavailable.")
    else:
        print(f"'{book_name}' is not in our library catalog.")

# Function to return a book
def return_book(book_name):
    if book_name in library_catalog:
        library_catalog[book_name]["copies_available"] += 1
        print(f"Thank you for returning '{book_name}'.")
    else:
        print(f"'{book_name}' does not belong to our library catalog.")

# Main program loop
def library_system():
    while True:
        print("\nWelcome to the Library System!")
        print("1. Display Available Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Exit")
        
        # Get user choice
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        
        # Selection structure to handle user input
        if choice == 1:
            display_books()
        elif choice == 2:
            book_name = input("Enter the name of the book you want to borrow: ")
            borrow_book(book_name)
        elif choice == 3:
            book_name = input("Enter the name of the book you want to return: ")
            return_book(book_name)
        elif choice == 4:
            print("Thank you for using the Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the library system
library_system()

"""
#------------------------------------------------------------------------------------------------------------------------------------------------------


'''Example #2''' #Creating a storage system for video game characters
# Dictionary to store video game characters
characters = {}

# Function to display all characters
def display_characters():
    if characters:
        print("\nVideo Game Characters:")
        for name, attributes in characters.items():
            print(f"Name: {name}, Class: {attributes['class']}, Level: {attributes['level']}, Abilities: {', '.join(attributes['abilities'])}")
    else:
        print("\nNo characters found. Create one to get started!")

# Function to add a new character
def add_character():
    name = input("\nEnter the character's name: ").strip()
    if name in characters:
        print("A character with this name already exists!")
        return
    char_class = input("Enter the character's class (e.g., Warrior, Mage, Archer): ").strip()
    level = int(input("Enter the character's level (1-99): ").strip())
    abilities = input("Enter the character's abilities (comma-separated): ").strip().split(",")
    characters[name] = {"class": char_class, "level": level, "abilities": [ability.strip() for ability in abilities]}
    print(f"Character '{name}' added successfully!")

# Function to update an existing character
def update_character():
    name = input("\nEnter the name of the character to update: ").strip()
    if name in characters:
        print("What would you like to update?")
        print("1. Class")
        print("2. Level")
        print("3. Abilities")
        choice = int(input("Enter your choice (1-3): "))
        if choice == 1:
            characters[name]["class"] = input("Enter the new class: ").strip()
        elif choice == 2:
            characters[name]["level"] = int(input("Enter the new level (1-99): ").strip())
        elif choice == 3:
            abilities = input("Enter the new abilities (comma-separated): ").strip().split(",")
            characters[name]["abilities"] = [ability.strip() for ability in abilities]
        else:
            print("Invalid choice. Returning to the main menu.")
            return
        print(f"Character '{name}' updated successfully!")
    else:
        print(f"Character '{name}' not found.")

# Function to remove a character
def remove_character():
    name = input("\nEnter the name of the character to remove: ").strip()
    if name in characters:
        del characters[name]
        print(f"Character '{name}' removed successfully!")
    else:
        print(f"Character '{name}' not found.")

# Main program loop
def character_management_app():
    while True:
        print("\nVideo Game Character Management")
        print("1. Display All Characters")
        print("2. Add a New Character")
        print("3. Update an Existing Character")
        print("4. Remove a Character")
        print("5. Exit")
        
        # Get user's choice
        try:
            choice = int(input("Enter your choice (1-5): ").strip())
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue
        
        # Selection structure to handle user input
        if choice == 1:
            display_characters()
        elif choice == 2:
            add_character()
        elif choice == 3:
            update_character()
        elif choice == 4:
            remove_character()
        elif choice == 5:
            print("Exiting the application. Thank you!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the application
character_management_app()


#------------------------------------------------------------------------------------------------------------------------------------------------------


'''Example #3''' #Creating a simple calculator
# Dictionary to store basic math operations
operations = {
    "1": {"name": "Addition", "function": lambda x, y: x + y},
    "2": {"name": "Subtraction", "function": lambda x, y: x - y},
    "3": {"name": "Multiplication", "function": lambda x, y: x * y},
    "4": {"name": "Division", "function": lambda x, y: x / y if y != 0 else "Undefined (cannot divide by zero)"}
}

# Function to display available operations
def display_operations():
    print("\nAvailable Operations:")
    for key, operation in operations.items():
        print(f"{key}. {operation["name"]}")

# Function to validate numeric input
def get_number(prompt):
    number = input(prompt).strip()
    while not number.replace(".", "", 1).isdigit():  # Ensure input is a valid number
        print("Invalid input. Please enter a numeric value.")
        number = input(prompt).strip()
    return float(number)

# Function to validate operation choice
def get_operation_choice():
    choice = input("Choose an operation (1-4): ").strip()
    while choice not in operations:
        print("Invalid choice. Please select a valid option.")
        choice = input("Choose an operation (1-4): ").strip()
    return choice

# Function to perform the chosen operation
def perform_operation(choice, num1, num2):
    result = operations[choice]["function"](num1, num2)
    print(f"Result: {result}")

# Main calculator function
def calculator():
    print("\nWelcome to the Simple Calculator!")
    while True:
        print("\nMain Menu:")
        print("1. Perform a Calculation")
        print("2. Exit")
        
        # Get user's main menu choice
        main_choice = input("Enter your choice (1-2): ").strip()
        while main_choice not in ["1", "2"]:
            print("Invalid input. Please select either 1 or 2.")
            main_choice = input("Enter your choice (1-2): ").strip()

        # Selection structure for main menu
        if main_choice == "1":
            # Display operations
            display_operations()
            
            # Get operation choice
            choice = get_operation_choice()
            
            # Get numeric inputs from the user
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            
            # Perform the operation
            perform_operation(choice, num1, num2)
        elif main_choice == "2":
            print("Goodbye! Thank you for using the Simple Calculator.")
            break

# Run the calculator
calculator()


#------------------------------------------------------------------------------------------------------------------------------------------------------


'''Example #4''' #Creating an exam scoring system
# Dictionary to store exam questions and answers
exam_questions = {
    1: {"question": "What is the capital of France?", "options": ["A. Berlin", "B. Paris", "C. Madrid", "D. Rome"], "correct": "B"},
    2: {"question": "What is 5 + 7?", "options": ["A. 10", "B. 12", "C. 13", "D. 14"], "correct": "B"},
    3: {"question": "Which programming language is primarily used for web development?", "options": ["A. Python", "B. C++", "C. JavaScript", "D. Java"], "correct": "C"},
    4: {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ["A. J.K. Rowling", "B. Harper Lee", "C. Ernest Hemingway", "D. Mark Twain"], "correct": "B"}
}

# Function to display a question
def display_question(question_num):
    question_data = exam_questions[question_num]
    print(f"\nQuestion {question_num}: {question_data['question']}")
    for option in question_data['options']:
        print(option)

# Function to validate the user's answer
def get_valid_answer():
    answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
    while answer not in ["A", "B", "C", "D"]:
        print("Invalid choice. Please enter A, B, C, or D.")
        answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
    return answer

# Function to grade the exam
def grade_exam(user_answers):
    score = 0
    for question_num, user_answer in user_answers.items():
        correct_answer = exam_questions[question_num]["correct"]
        if user_answer == correct_answer:
            score += 1
    return score

# Main exam practice function
def exam_practice():
    print("\nWelcome to Exam Practice!")
    user_answers = {}
    
    # Loop through all questions
    for question_num in exam_questions:
        display_question(question_num)
        user_answer = get_valid_answer()
        user_answers[question_num] = user_answer
    
    # Grade the exam
    score = grade_exam(user_answers)
    print(f"\nYou answered {score}/{len(exam_questions)} questions correctly!")
    if score == len(exam_questions):
        print("Excellent work!")
    elif score >= len(exam_questions) // 2:
        print("Good job! Keep practicing.")
    else:
        print("Don't worry. Practice makes perfect!")

# Run the exam practice application
exam_practice()"
"""