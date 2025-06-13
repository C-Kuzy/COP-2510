'''
 Name: Connor Kouznetsov
 Description: Week 10 Lecture 1 Notes, understanding lists, if then statements, and other things
'''

#Recap amongst string slicing
name = "Connor Kouznetsov"
sn1 = name[5: 11] #The start position is 5 (is inclusive); end position is 10 (11 is exclusive)
print(sn1)

#We can use -ve indicies as well to determine starting and ending positions

sn2 = name[-5: -2]
print(sn2)

#We can oit the starting and ending positions

sn3 = name[4: ]
print(sn3)
sn4 = name[:-4]
print(sn4)

#See section 6.4 , 8.3, 8.13 for additional methods

#list coprehension - create a new list from an exisitng list

list1 = [10, 20, 30, 40, 50]
list2 = [i/5 for i in list1]
print(list2)

#list comprehension with ternary form

list3 = [j/2 if j > 30 else j * 4 for j in list1] #ternary form
print(list3)

#list comprehension with the if statement

list4 = [k/10 for k in list1 if k <= 20] #The if statement is last and can affect the size of the list
print(list4)

#Python will allow for dictonary comprehension

newdiction = {n: n**3 for n in range(10)}
print(newdiction)


#File i/o
dogfile = open()
