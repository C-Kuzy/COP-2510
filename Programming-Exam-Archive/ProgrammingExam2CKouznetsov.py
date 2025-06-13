'''
 Author: Connor Kouznetsov
 Description: My program is responsible for determining/calculating a rogue buyer's value shopping spree
'''

'''THIS IS PART 1: THE CLASS PORTION OF MY CODE!!!'''

# #1: Creating the Parent Class = "Spree" (DONE)
class Spree:
    # #2: Create class variable (budget, make this updated variable = 0)
    budget = 0
    # #3: Using initlaizer method, use 2 parameters (1: name_of_store or nos, 2: total_price_paid or tpp)
    def __init__(self, nos, tpp):
        self.__name_of_store = nos
        self.__total_price_paid = tpp

    # #4: Use Accessor Method(s) (Getter Functions)
    def get_tpp(self):
        return self.__total_price_paid
    
# #5: Create Mutator Method(s) (Setter Functions) (USE @CLASSMETHOD FROM WEEK13LECTURENOTE1)
    @classmethod
    def set_user_spending_budget(cls, new_usb): #Use of cls represents an input class as first parameter
        cls.budget = new_usb

#6 Create str method that returns the hidden attributes
    def __str__(self):
        return f"Store Visited: {self.__name_of_store}\nTotal Amount Spent: ${self.__total_price_paid}" 

'''THIS IS PART 2: THE DRIVER PORTION OF MY CODE!!!'''

# #7: First Function, Creating The List of Shopping Spree Objects (mainfunct() = build_obj_n_spree())
def build_obj_n_spree(amount_of_stores):
    shopping_spree_list = []
    for _ in range(amount_of_stores):
        nos = input("Store Name: ")
        tpp = float(input("Total Amount Spent Here (in $ or dollars):"))
        spree = Spree(nos, tpp)
        shopping_spree_list.append(spree)
    return shopping_spree_list

def find_total_price(shopping_spree_list): #we need to use math function of sum
    total_spent = sum(spree.get_tpp() for spree in shopping_spree_list)
    return total_spent

def finalized_view_shop_spree(shopping_spree_list):
    for spree in shopping_spree_list:
        print(spree)

def mainfunct():
    user_budget = float(input("Input today's Shopping Spree Budget ($): "))
    Spree.set_user_spending_budget(user_budget)

    num_of_stores = int(input("Input how many stores you visited Today!: "))

    shopping_spree_list = build_obj_n_spree(num_of_stores)
    print(f"Your Available Budget: ${Spree.budget:,.2f}") #start of the list

    finalized_view_shop_spree(shopping_spree_list)
    spent_total_amt = find_total_price(shopping_spree_list)

# #15: With Total Spent, use "if-else" to display message indicate if within budget
    if spent_total_amt <= Spree.budget:
        print(f"Good Job! You managed to spend within the budget!.")
    else:
        user_over_budget = (spent_total_amt - Spree.budget)
        print(f"Whoops, you overspent your budget by ${user_over_budget:,.2f}.")

if __name__ == "__main__":
    mainfunct()