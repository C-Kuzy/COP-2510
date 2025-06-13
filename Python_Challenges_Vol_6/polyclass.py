'''
 Author: Connor Kouznetsov
 Description: My program is responsible for calculating the Area and Perimeter of an 'n' sided polygon.
'''
#Ensure that "import math" is included to execute math statements
import math

#Start the program by defining the class Polygon side lengths
class Polygon():
    #Setting the Number and Length of Sides to a default value of "0"
    def __init__(self):
        self.__number_Of_Sides = 0
        self.__side_Length = 0.0

    #Create necessary Accessor Methods
    def Get_NumberOfSides(self):
        return self.__number_Of_Sides
    
    def Get_SideLength(self):
        return self.__side_Length
    
    #Create necssary Mutator Methods
    def Set_NumberOfSides(self, number_Of_Sides):
        self.__number_Of_Sides = number_Of_Sides

    def Set_SideLength(self, side_Length):
        self.__side_Length = side_Length

    #Create the Calculation for both Perimeter & Area of the Function
    def CalculateAreaOfPolygon(self):
        return ((self.__side_Length ** 2) * self.__number_Of_Sides) / (4 * math.tan(math.pi / self.__number_Of_Sides))

    def CalculatePerimeterOfPolygon(self):
        return ((self.__side_Length) * (self.__number_Of_Sides))

def mainfunct():
    shape = Polygon()
    while True:
        try:
            number_Of_Sides = int(input("Enter the number of sides of your polygon (>=3):"))
            if number_Of_Sides >= 3:
                shape.Set_NumberOfSides(number_Of_Sides)
                break
            print("Not Valid! Please enter a number greater than or equal to 3.")
        except:
            continue
    
    while True:
        try:
            side_Length = float(input("Enter the length of the sides of your polygon (>=0.1):"))
            if side_Length >= 0.1:
                shape.Set_SideLength(side_Length)
                break
            print("Not Valid! Please enter a number greater than 0.1.")
        except:
            continue

    print(f"The number of sides of the polygon is {shape.Get_NumberOfSides()}")
    print(f"The length of the sides of the polygon is {shape.Get_SideLength():.3f}")
    print(f"The area of the polygon is {shape.CalculateAreaOfPolygon():.3f}")
    print(f"The perimeter of the polygon is {shape.CalculatePerimeterOfPolygon():.3f}")

mainfunct()