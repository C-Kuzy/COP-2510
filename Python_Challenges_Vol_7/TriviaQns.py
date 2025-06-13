'''
 Author: Connor Kouznetsov
 Description: The use of this program allows us to create our necessary questions that will be answered by the guest players.
'''

from Question import Question

def trivia_qns():
    available_qns_prompts = [
        Question("Which sport is the most popular in the world?"
        ,"1:Soccer", "2:Hockey", "3:Golf", "4:Tennis", 1), 
        Question("What is the most popular car rim size?", "1:17 inch", 
                 "2:18 inch", "3:19 inch", "4:20 inch", 2), 
        Question("Who won the 2018 Stanley Cup Final?", "1:Washington Capitals",
                 "2:Vegas Golden Knights", "3:Chicago Blackhawks", "4:New York Rangers", 1), 
        Question("What is the Royal Caribbean Cruise Line's largest cruise ship?",
                 "1:Harmony of the Seas", "2:Symphony of the Seas", "3:Oasis of the Seas", "4:Icon of the Seas", 4), 
        Question("What is the most popular Yeezy model ever sold?", "1:Yeezy 350", 
                 "2:Yeezy 500", "3:Yeezy 700", "4:Yeezy 750", 1), 
        Question("Which food would you most likely expect to find at a resturant?", 
                 "1:Pizza", "2:Pasta", "3:Salad", "4:All of the above", 4), 
        Question("How often is it recommended that you need to change your car's oil?", 
                 "1:Every 3,000 miles", "2:Every 5,000 miles", "3:Every 7,500 miles", "4:Every 10,000 miles", 2), 
        Question("What is the most popular programming language in the world?", 
                 "1:Python", "2:Java", "3:JavaScript", "4:C++", 1), 
        Question("What is the most popular social media platform in the world?", 
                 "1:Facebook", "2:Instagram", "3:Twitter", "4:TikTok", 1), 
        Question("What is the answer to this equation?: 1 + 1", 
                 "1:1", "2:2", "3:3", "4:4", 2)
    ]
    return available_qns_prompts