# WEEK 8 lecture 1
# FUNCTIONS

# Value returning function

def tripval(num):

    num *= 3# NUM IS LOCAL TO THIS 
    return num



# function that does not return a value
def info():
    print('This is an example of a function that does not returna value')
    print('or use a return keyword')
    
# basically running it through
#the code reads the func
# the and sees n then puts n
# through the funct bc print



# main portion
def main():
    n = int(input('Enter a number:'))
    #print(f'The value tripled is {tripval(n)}')
    newn = tripval(n)#IMPORTANT                 
    print(f'The value tripled is {newn}')
    
    info()# gives none when printed because the value is technichally none

#second version of main
def main():
    print('This is second main')

# call to main()
main()# basically just organizes the code 
#Identifier naming rules apply









