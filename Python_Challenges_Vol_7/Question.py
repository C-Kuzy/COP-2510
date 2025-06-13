'''
 Author: Connor Kouznetsov
 Description: This purpose of this code is to create a class: "Questions" that is responsible for creating an object that
              stores the question, the answer, and other possible choices. We need to use the __init__ method to intialize our object.
'''
#Create our class
class Question:
    #Now using a define function, we need to initialize "__init__" our object
        def __init__(self, question, aswr1, aswr2, aswr3, aswr4, answer_correct):
                
                #NOW STORE THE VARIABLES IN THE OBJECT
                self.__question = question
                self.__aswr1 = aswr1
                self.__aswr2 = aswr2
                self.__aswr3 = aswr3
                self.__awsr4 = aswr4
                self.__answer_correct = answer_correct

        #Create necessary Accessor Methods
        #Accessor get question
        def get_question(self):
                return self.__question
        
        #Accessor get answer 1
        def get_answer_right(self):
                return self.__answer_correct
        
        #Create necessary __str__ method to return a string representation of the object
        def __str__(self):
                return f"{self.__question}\n{self.__aswr1}\n{self.__aswr2}\n{self.__aswr3}\n{self.__awsr4}\n{self.__answer_correct}"