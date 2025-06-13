'''
 Author: Connor Kouznetsov
 Description: Week 12, Lecture 2 on Thursday Nov 14th
'''

#Class Module Example
#parent (super, base) class

class Vehicle:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def getmake(self):
        return self.__make
    
    def getmodel(self):
        return self.__model

    def getyear(self):
        return self.__year

#child (sub, derived) class
class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        Vehicle.__init__(self, make, model, year)

        self.__doors = doors #one_ means protected attribute

    def getdoors(self):
        return self.__doors
    
#child class of child class (tiered single inheritance)
class ElectricCar(Car):
    def __init__(self, make, model, year, doors, voltage):
        Car.__init__(self, make, model, year, doors)

        self.__voltage = voltage
    
    def getvoltage(self):
        return self.__voltage
    
#-------class definition ends here-------

#driver portion of the program
#create Vehicle object
v1 = Vehicle("Hyundai", "Elantra", 2023)
print(f"My friend drives a {v1.getyear()} {v1.getmake()} {v1.getmodel()}.")

#create Car object
c1 = Car("Toyota", "Camry", 2024, 4)
print(f"My friend drives a {c1.getyear()} {c1.getmake()} {c1.getmodel()} with {c1.getdoors()} doors.")

#create EletricCar object
e1 = ElectricCar("Tesla", "Model S", 2025, 4, 100)
print(f"My friend drives a {e1.getyear()} {e1.getmake()} {e1.getmodel()} with {e1.getdoors()} doors and a voltage of {e1.getvoltage()} volts.")



