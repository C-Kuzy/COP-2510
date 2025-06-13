# Week 12 Lecture 2

# examples of a parent class, child class,  

# used for software reuse

#parent(super,base) class

class Vehicle:
    def __init__(self,make,model,year):
        self.__make = make
        self.__model = model
        self.__year = year

    def getMake(self):
        return self.__make

    def getModel(self):
        return self.__model

    def getYear(self):
        return self.__year


#THIS IS INHERITANCE    
#child(sub,derived) class
class Car(Vehicle):
    def __init__(self,make,model,year,doors):

        #accesses the attributes from the parent
        Vehicle.__init__(self,make,model,year)

        # this is for doors in here
        
        self._doors = doors # ONE _ makes the attribute protected and can be
                            # directly accessed with in the class and to
                            # its children

    def getDoors(self):
        return self._doors



#Child class of child class(AKA tiered single inheritance)

class ElectricCar(Car):
    def __init__(self,make,model,year,doors,bvolt):

        # See how when u call the class you put every attribute
        Car.__init__(self,make,model,year,doors)


        self.__bvolt = bvolt

    def getBvolt(self):
        return self.__bvolt



#-----class definition ends ------

#Driver portion
#create Vehicle object

v1 = Vehicle('Hyundai','Elantra',2023)
#REMEMBER TO PUT THE () TO CALL THE GETTER FUNCTS
print(f' My friend drives a {v1.getYear()} {v1.getMake()} {v1.getModel()}')

#create Car Object
c1 = Car('Honda','Civic',2019,4)
print(f' I drive a {c1.getYear()} {c1.getMake()} {c1.getModel()} with {c1.getDoors()} doors')

# Inheritance is basically an extension of a class in the fact that
# all the attributes in Vehicle it is able to be refrenced in Car

# NOTE CHILDS CAN BECOME PARENTS

#Create ElectricCar Obj
e1 = ElectricCar('Checy','Volt',2025,4,80)

#using a \ with a enter continues the print
print(f' my bro drives a {e1.getYear()} {e1.getMake()} {e1.getModel()} with {e1._doors} doors \
with {e1.getBvolt()} volts')



'''Go on modules for another set of classes
 the one for compostion shows  an object being created in
 another object.
 That IS NOT INHERITANCE if anything its more complcated
 

 Aggregation is another form



 MAIN DIFFERENCES
 Composition
 The objects are dependent on each other

 Aggregation
 The objects can be used independently or both together
'''
# geekforgeeks.org




