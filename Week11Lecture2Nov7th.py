'''
 Name: Connor Kouznetsov
 Description: Class Returns after 2nd hurricane! 
'''
'''
#how not to create a class 
class Test:
    pass

def main():
    testobj = Test()
    print(testobj)
    testobj.name = "Connor"
    print(f"{testobj.name}")

main()
'''

##############################################
'''Here's a better way to create a class'''

class Television:
    
    #Initializer Method (Helps us with setting up the object)
    #Self - This is a placeholder for the object
    #Attributes - These are the characteristics of the object: aka Channel, Volume, & Power
    #__ means that we keep the attribute private or hidden
    def __init__(self):
        self.__channel = 1
        self.__volume = 1
        self.__power = False

    #Accessor (Getter) Methods
    def getchannel(self):
        return self.__channel

    def getvolume(self):
        return self.__volume

    def getpower(self):
        if self.__power:
            status = "On"
        else:
            status = "Off"
        return status

    #Mutator (Setter) Methods
    def setchannel(self, ch):
        self.__channel = ch

    def setvolume(self, vol):
        self.__volume = vol

    def setpower(self, p):
        self.__power = p

    #Other Methods


    #Str Method
    def __str__(self):
        return f"TV stats:\nPower: {self.getpower()}\nChannel: {self.__channel}\nVolume: {self.__volume}"

#---End of class definition---#

#Create an appropriate Television Object
tv1 = Television() #init method is automaticlaly called when the object is created
'''tv1= Television(201, 15, True)'''

#Testing our str method (this is called automatically when an object is passed through a print statement)
print(tv1)
'''print()'''

#Test all mutators
tv1.setpower(True)
tv1.setchannel(60)
tv1.setvolume(12)

#Test all accessors
print(f"The tv1 object is {tv1.getpower()} and it is on channel {tv1.getchannel()}.")
print(tv1)