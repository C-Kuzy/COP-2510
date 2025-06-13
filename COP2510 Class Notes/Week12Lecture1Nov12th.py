'''
 Author: Connor Kouznetsov
 Descritpion: Week 12, Lecture 1 on Tuesday November 12th, 2024 Notes!
'''

#Class Module Example

class Show:
    numShows = 0 #This represents the class variable

    def __init__(self, sName, sType):
        self.__showName = sName #Attributes (creating an instance variable for the object)
        self.__showType = sType #Attributes (creating an instance variable for the object)
        Show.numShows += 1
    
    def __str__(self):
        return f"{self.__showName} is a {self.__showType} show."
    
show1 = Show('The Office', 'Comedy')
print(show1.showName)
print(f"There are {Show.numShows} pbjects(s) created so far.")
show2 = Show('Breaking Bad', 'Drama')
print(f"There are {Show.numShows} objects(s) created so far.")

#Driver Module Example

#Create a function that creates a list of objects
def showList(n):
    slist = []

    for i in range(n):
        showname = input("Show Name: ")
        showtype = input("Show Genre: ")
        print()
    
        #Create an object for the shows
        sobj = Show(showname, showtype)

        #Add an object to the list of objects
        slist.append(sobj)

    return slist

#Now return a function that displays the list
def displayShows(slist):
    for s in slist:
        print(s)
    
#Main Portion of the program
number = int(input("Enter number of shows: "))

#Call showList function
shows = showList(number)

#Now Echo Print the List of Objects (using displayShows function)
displayShows(shows)
print(f"There are {Show.numShows} object(s) created so far.")
print(f"There are {shows[1].getNumShows()} object(s) created so far.")

Show.numShows += 10
print(f"There are {Show.numShows} object(s) creates so far.")