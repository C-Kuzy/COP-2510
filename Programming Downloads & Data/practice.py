
##
##class TaskManager:
##    
##    def __init__(self):
##        self.__tasks = []
##
##
##    def add_task(self,task):
##        self.__tasks.append(task)
##
##
##    def remove_task(self,task):
##        if task in self.__tasks:
##            self.__tasks.remove(task)
##        else:
##            print('task does not exist')
##        
##    def show_tasks(self):
##        if len(self.__tasks) == 0:
##            print('No tasks to show')
##
##        else:
##            for i in self.__tasks:
##                print(i)
##
##
##def main():
##    tasks = TaskManager()
##
##    tasks.add_task(input('input task'))
##    tasks.add_task(input('input task'))
##    tasks.add_task(input('input task'))
##
##    tasks.remove_task(input('input task to remove'))
##
##    tasks.show_tasks()
##
##main()


##class Book:
##
##    def __init__(self,title,author,year):
##        
##        self._title = title
##
##        self._author = author
##
##        self._year = year
##
##
##    #Mutators
##    def set_title(self,title):
##        self._title = title
##    def set_author(self,author):
##        self._author = author
##    def set_year(self,year):
##        self._year = year
##    #Accessors
##
##    def get_title(self):
##        return self._title
##
##    def get_author(self):
##        return self._author
##    def get_year(self):
##        return self._year
##    #str
##    def __str__(self):
##        return f'Title: {self._title} author: {self._author} \
##year: {self._year}'
##    
##class Ebook(Book):
##
##    def __init__(self,title,author,year,file_size):
##        self.__size = (file_size)
##
##        Book.__init__(self,title,author,year)
##
##    def set_file_size(self,file_size):
##        self.__size = file_size
##
##    def get_file_size(self):
##        return self.__size
##
##    def __str__(self):
##        return f'{Book.__str__(self)} file size: {self.__size}'
##
##class Library:
##    def __init__(self):
##        self.__catalog = []
##        
##    def add_book(self,book):
##        self.__catalog.append(book)
##        
##    def display_books(self):
##        for i in self.__catalog:
##            print(i)
##
##
##
##
##def main():
##
##    cat = Library()
##    
##    num = int(input('Enter the amount of books you want to enter'))
##    
##    while num < 1:
##        num = int(input('invalid enter amount'))
##
##    for i in range(num):
##        
##        what_is_book = int(input('what is book 1- electronic 2- regular'))
##        
##        while what_is_book < 1 or what_is_book > 2:
##            what_is_book = int(input('invalid input 1 or 2'))
##
##        if what_is_book == 1:
##            title = input('what is title')
##            author = input('who is the author')
##            year = int(input('what year published'))
##            file_size = float(input('what is the size'))
##            
##            book = Ebook(title,author,year,file_size)
##            cat.add_book(book)
##        else:
##            title = input('what is title')
##            author = input('who is the author')
##            year = int(input('what year published'))
##            
##            book = Book(title,author,year)
##            cat.add_book(book)
##    print('Books in the Library:')
##    cat.display_books()
##    
##
##    
##main()
##    

import math

# Total days on Planet X
days = 45

# Function to compute the probability that at least two people share a birthday
def birthday_probability(n, days):
    prob_unique = 1.0
    for k in range(n):
        prob_unique *= (days - k) / days
    return 1 - prob_unique

# Find the minimum number of people such that probability >= 0.6
for n in range(1, days + 1):
    prob = birthday_probability(n, days)
    if prob >= 0.6:
        print("Minimum number of people:", n)
        print("Probability: {:.4f}%".format(prob * 100))
        break
































