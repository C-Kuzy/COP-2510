'''
 Author: Connor Kouznetsov
 Description: September 17th, 2024, Week 4 Lecture 1
'''

#Intro to types: Strings, Lists, Tuples, Sets, Dictionaries

#Strings - Sequence Type - Contents are ordered access contents using index
#Strings are immutable (can't be changed)
name = "Connor"
print(name[0]) #first position is 0
print(name[-1]) #last position is -1
print(name[5]) #last position of this value is 'r'
print(name[-7]) #index out of range
name[-1] = 'L' # does not work because strings are immutable

print(len(name)) #length of the string

#strings can be added (concatenation)
first = 'Monty'
last = 'Python'
full = first + last

#use * for dups
print(first * 3)

#string slicing (ending index is exclusive)
test = first[0:3] + ' ' + last[-3:-1] #slicing
print(test)

#Lists are containers: They can hold multiple different types of data
#Lists are also considered a sequence type: Where contents are ordered
#Lists are mutable: The values can be changed
x = 5
items = [] #empty list
items = ['cheese', 'eggs', 'bacon', 1, True, 5.9, ['Tampa', 'Florida', 17]]
print(items)
print(items[2])

items[1] = 'milk'

#list methods: append, pop, remove
items.append('cookies') #insertion at the end of the list

##print(items)

##print(itmes[-2][0]) #accessing the nested list components, repeat once more for further access

##items.pop()
##print(items)
##items.pop(4)
##print(items)
##items.remove('bacon')
##print(items)

#Tuples are sequences and containers, but are immutable
##somemore = (1, 5.9, 'something')
##print(somemore[1])
#somemore[1] = 6.9 #does not work because tuples are immutable
##tu =(1,)


#Sets are an unordered collection of unique elements
#Sets are containers, but not sequences. THey are also mutable.
##s1 = {1.0, 'two', 3.0, '1', 4, 5.0}
##print(s1)
##print(s1[0]) #This function does not work

#Dictonaries are containers, but not sequences. They are used for associative relationships
'''#They are a mapping type that is mutable
alias = {'cat': 'floof', 1:['one', 1.0, '1'], 'five': (5, 5.0)}
print(alias['cat'])
print(alias[1][2])
print(alias.keys())
print(alias.items())
print(alias.values())'''

#Selection: if, if-else, if-elif-else
#Rely on conditions that must evaluate to True or False
#Define conditions within relational and/or logical operators
#Relational operators: ==, !=, <, >, <=, >=

