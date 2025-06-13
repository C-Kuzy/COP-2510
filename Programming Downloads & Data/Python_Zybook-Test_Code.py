#CODE SERIES NUM-1
'''
def find_ticket_fee(person_age):
    if (person_age > 79 or person_age < 5):
        return 2
    elif (17 <= person_age <= 59):
        return 26
    else:
        return 17

input_person_age = int(input())

print(f'Testing 83: {find_ticket_fee(83)}')
print(f'Testing user input: {find_ticket_fee(input_person_age)}')
'''
#CODE SERIES NUM-2
'''
def print_values(number1, number2):
    for number in range(number1, number2 + 1):
        print(number, end=' ')

number1 = int(input())
number2 = int(input())

print('Testing static input: ')
print_values(4, 6)
print(f'\nTesting user input: ')
print_values(number1, number2)
'''
#CODE SERIES NUM-3
'''
def celsius_to_kelvin(value_celsius):
    value_kelvin = 0.0

    value_kelvin = value_celsius + 273.15
    return value_kelvin

def kelvin_to_celsius(value_kelvin):
    value_celsius = 0.0
    
    value_celsius = value_kelvin - 273.15
    return value_celsius

value_c = 10.0
print(f'{value_c} C is {celsius_to_kelvin(value_c)} K')

value_k = float(input())
print(f'{value_k} K is {kelvin_to_celsius(value_k)} C')
'''
#CODE SERIES NUM-4
'''
# FIXME: Write the split_check function. HINT: Calculate the amount of tip and tax,
# add to the bill total, then divide by the number of diners.

def split_check(bill, people, tax_percentage = 0.09, tip_percentage = 0.15):
    tip_amount = bill * tip_percentage
    tax_amount = bill * tax_percentage
    total_bill = bill + tip_amount + tax_amount
    cost_per_diner = total_bill / people
    return cost_per_diner

bill = float(input())
people = int(input())

# Cost per diner at the default tax and tip percentages
print(f'Cost per diner: ${split_check(bill, people):.2f}')

bill = float(input())
people = int(input())
new_tax_percentage = float(input())
new_tip_percentage = float(input())

# Cost per diner at different tax and tip percentages
print(f'Cost per diner: ${split_check(bill, people, new_tax_percentage, new_tip_percentage):.2f}')
'''
#CODE SERIES NUM-5
'''
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    cost = (miles_driven / miles_per_gallon) * dollars_per_gallon
    return cost

if __name__ == '__main__':
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())

    cost_10_miles = driving_cost(miles_per_gallon, dollars_per_gallon, 10.0)
    cost_50_miles = driving_cost(miles_per_gallon, dollars_per_gallon, 50.0)
    cost_400_miles = driving_cost(miles_per_gallon, dollars_per_gallon, 400.0)

    print(f'{cost_10_miles:.2f}')
    print(f"{cost_50_miles:.2f}")
    print(f"{cost_400_miles:.2f}")
'''
#CODE SERIES NUM-6
'''
# Define your function here 
def feet_to_steps(feet):
    steps = feet / 2.5
    return int(steps)

if __name__ == '__main__':
    feet_walked = float(input())
    steps_walked = feet_to_steps(feet_walked)
    print(f"{steps_walked}")
'''
#CODE SERIES NUM-7
