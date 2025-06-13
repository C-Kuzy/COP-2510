"""
 Author: Connor Kouznetsov
 Description: This is a python practice file for ZyLab's under Activity #5
"""

'''*****Zylab 4.13 Remove gray from RGB*****'''

#Given integer values for red, green, and blue, subtract the gray from each value. 
#Reference #1: Bright Red = (255, 0, 0), Reference #2: Medium Purple = (130, 0, 130), Reference #3: Black = (0, 0, 0)
#Reference #4: White = (255, 255, 255), Reference #5: Dark Gray = (50, 50, 50), Reference #6: Faded Purple = (130, 50, 130)

#We know that the gray part is (R: 50, G: 50, B: 50) and we can subtract this from the RGB values given
'''
Color_Red = int(input())
Color_Green = int(input())
Color_Blue = int(input())

if not all(0 <= Color_Val <= 255 for Color_Val in [Color_Red, Color_Green, Color_Blue]):
    False
else:
    gray = min(Color_Red, Color_Green, Color_Blue)
    Color_Red -= gray
    Color_Green -= gray
    Color_Blue -= gray
print(f"{Color_Red} {Color_Green} {Color_Blue}")
'''

'''*****Zylab 4.16 Leap Year Calculator*****'''

'''is_leap_year = False
   
input_year = int(input())

def is_leap_year(year):
    if input_year % 4 == 0:
        if input_year % 100 == 0:
            if input_year % 400 == 0:
                return True
            else:
                return False  
        else:
            return True 
    else:
        return False  

if is_leap_year(input_year):
    print(f"{input_year} - leap year")
else:
    print(f"{input_year} - not a leap year")
    '''


'''*****ZyLab 4.17 Golf Scores*****'''
'''
def golf_score(strokes, par):
    if par not in [3, 4, 5]:
        print(f"Par {par} in {strokes} strokes is Error")
        return

    difference = strokes - par

    if difference == -2:
        score_name = "Eagle"
    elif difference == -1:
        score_name = "Birdie"
    elif difference == 0:
        score_name = "Par"
    elif difference == 1:
        score_name = "Bogey"
    else:
        score_name = "Error"

    print(f"Par {par} in {strokes} strokes is {score_name}")

# Example usage:
strokes = int(input())
par = int(input())
golf_score(strokes, par)
'''


'''*****ZyLab 4.19 Automobile Service Cost*****'''

services = {
    "Oil change": 35,
    "Tire rotation": 19,
    "Car wash": 7
}

service = input("Enter desired auto service:\n")

print(f"You entered: {service}")

if service in services:
    print(f"Cost of {service.lower()}: ${services[service]}")
else:
    print("Error: Requested service is not recognized")


'''*****ZyLab 4.20 Automobile Service Invoice*****'''

#Step 1: Output the menu of automotive services
services = {
    "Oil change": 35,
    "Tire rotation": 19,
    "Car wash": 7,
    "Car wax": 12
}

def print_menu():
    print("Davy's auto shop services")
    for service, cost in services.items():
        print(f"{service} -- ${cost}")
    print()

#Step 2: Prompt the user for two services
print_menu()
service1 = input("Select first service:\n")
service2 = input("Select second service:\n")

#Step 3: Output the invoice
print("\nDavy's auto shop invoice\n")

def print_service(service_name):
    if service_name == "-":
        return "No service"
    elif service_name in services:
        return f"{service_name}, ${services[service_name]}"
    else:
        return "Invalid service"

service1_output = print_service(service1)
service2_output = print_service(service2)

print(f"Service 1: {service1_output}")
print(f"Service 2: {service2_output}")

#Step 4: Calculate and output the total cost
def calculate_total():
    total = 0
    if service1 in services:
        total += services[service1]
    if service2 in services:
        total += services[service2]
    return total

total_cost = calculate_total()
print(f"\nTotal: ${total_cost}")