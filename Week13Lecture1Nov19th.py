'''
Author: Connor Kouznetsov
Description: Week 13, Lecture 1 on Tuesday Nov 19th
'''

#Creating parent classes Example
'''
class Animal:
    def __init__(self, name):
        print(f"{name} is an animal.")
        super().__init__(name)  #comment out when using part 2

class HatesWaterBaths:
    def __init__(self, name):
        print(f"{name} hates getting a bath.")
        super().__init__(name)  #comment out when using part 2

class LovesToSunBathe:
    def __init__(self, name):
        print(f"{name} loves to lay and sunbathe.")

#Creating child classes Example
class Dog1(Animal, HatesWaterBaths, LovesToSunBathe):
    def __init__(self, name):
        print(f"{name} is a dog.")
        super().__init__(name)
'''      
#Can also swap the order of the parent classes: Part 1
'''
class Dog2(HatesWaterBaths, LovesToSunBathe, Animal):
    def __init__(self, name):
        print(f"{name} is a dog.")
        super().__init__(name)

class Dog3(LovesToSunBathe, Animal, HatesWaterBaths):
    def __init__(self, name):
        print(f"{name} is a dog.")
        super().__init__(name)
'''
#Can also use the following order to work with identifying classes: Part 2
'''
class Dog1(Animal, HatesWaterBaths, LovesToSunBathe):
    def __init__(self, name):
        print(f"{name} is a dog.")
        Animal.__init__(self, name)
        HatesWaterbaths.__init__(self, name)
        LovesToSunBathe.__init__(self, name)

class Dog2(HatesWaterBaths, LovesToSunBathe, Animal):
    def __init__(self, name):
        print(f"{name} is a dog.")
        HatesWaterbaths.__init__(self, name)
        LovesToSunBathe.__init__(self, name)
        Animal.__init__(self, name)

class Dog3(LovesToSunBathe, Animal, HatesWaterBaths):
    def __init__(self, name):
        print(f"{name} is a dog.")
        LovesToSunBathe.__init__(self, name)
        Animal.__init__(self, name)
        HatesWaterbaths.__init__(self, name)

'''
#Creating the Driver Portion of the Program
##dog = Dog1("Deez Nutz")
##dog = Dog2("Ur Mom")
##dog = Dog3("Ur Dad")

'''EXAMPLE 2, WORKING WITH CLASSMETHODS'''
#About @classmethod (this is preferred over using '''classmethod()''')
class LoLPlayer:
    name = "False"  #class attribute

    def __init__(self):
        self.role = "Mid Lane"  #instance attribute/variable

    @classmethod
    def about(cls): #cls - first parameter (represents an input class name)
        print(f"{cls.name} is one of the best LoL players in the world.")
        #cls.name = "Faker, the GOAT"

    @staticmethod
    def moreinfo():
        name = "Deft"
        print(f'{LoLPlayer.name} is sometimes called "Unkillable Demon King".')
        print(f'{name} is sometimes called "Unkillable Demon King".')

#Form the driver portion of the program
LoLPlayer.about() #calling the class method using the class name

lolpl = LoLPlayer() #creating an object of the class
lolpl.about() #calling the class method using the object name

#calling the static method using the class name
LoLPlayer.moreinfo() #calling the static method using the class name
lolpl.moreinfo() #calling the static