'''
 Author: Connor Kouznetsov
 Description: The purpose of this program is to ensure that our user is able to actually play our game.
            In order to do this, we'll need to import the file(s) which contain our question variables.
            This will hopefully allow the user to play the game and answer the questions with accuracy.
'''
from TriviaQns import trivia_qns

def mainfunct():
    available_qns_prompts = trivia_qns()

    print("WELCOME to a classic game of TRIVIA!")
    print("Lets begin by stating the only rule the game...")
    print("You'll be asked a series of questions and you need to answer them correctly.")

    guestOne_pts = 0
    guestTwo_pts = 0

    for w, available_qns_prompts in enumerate(available_qns_prompts):
        selected_guest_player = 2
        if w % 2 == 0:
            selected_guest_player = 1

        print(f"Player{selected_guest_player}'s Turn","\n")
        print(available_qns_prompts)

        #create a input to select an answer choice to a question
        quest_answr = int(input("Select a number you think is the answer (1-4):"))

        #use input validity to check false inputs 
        while quest_answr <= 0 or quest_answr >= 5:
            quest_answr = int(input("INVALID ENTRY!!! Choose a valid answer option(1-4):"))
        
        if quest_answr == available_qns_prompts.get_answer_correct():
            if selected_guest_player == 1:
                guestOne_pts +=1
                print("You got it Correct!!","\n")
            
            if selected_guest_player == 2:
                guestTwo_pts +=1
                print("You got it Correct!!","\n")

        else:
            print("Sorry, the answer you gave us was Incorrect!!","\n")
            print(f'The correct answer was answer number {available_qns_prompts.get_answer_correct()}',"\n")

    #Create print statements to display this programs final output
    print(30 * "-")
    print("Now that we have finished our set of questions. Let's now get each guest contestants total!","\n","THE FINAL SCORES ARE IN!!")
    print(30 * "-","\n")

    #This code is not part of the for loop, this is to calculate the final points between the two Guest Players.
    if guestTwo_pts < guestOne_pts:
        print(f"Guest 1 Wins with {guestOne_pts}")
        print(f"\n","Guest 1 earned {guestOne_pts})}")
        print(f"Guest 2 earned {guestTwo_pts}")
    
    elif guestOne_pts < guestTwo_pts:
        print(f"Guest 2 Wins with {guestTwo_pts}")
        print(f"\n","Guest 1 earned {guestOne_pts}")
        print(f"Guest 2 earned {guestTwo_pts}")

    elif guestOne_pts == guestTwo_pts:
        print("IT LOOKS LIKE WE HAVE A TIE!!","\n","In this case, both guest contestants are crowned the winners!!")
    
    else:
        print("We have an error, please start over!!")
             
mainfunct()