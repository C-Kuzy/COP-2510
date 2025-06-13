'''
 Author: Connor Kouznetsov
 Description: My program will use a bar chart to calculate the # of points scored by active players on a basketball team.
'''

#Begin and import necessary modules
import matplotlib.pyplot as plt

#Define the function 'PlayerNames'
def participant_names():
    Athletes = []
    for k in range(1, 6):
        name = input(f"Enter the name of player {k}: ")
        Athletes.append(name)
    return Athletes

def participant_points(Athletes):
    Points = []
    for Athletes in Athletes:
        while True:
            try:
                Athlete_Points = int(input("Enter the total amount of points {Athlete} scored: "))
                if Athlete_Points < 0:
                    print("Not Valid! Please enter a number greater than or equal to 0.")
                else:
                    Points.append(Athlete_Points)
                    break
            except:
                print("Not Valid! Please enter a valid integer or points.")
    return Points

def bar_chart(Athletes, Points):
    plt.bar(Athletes, Points, color = 'red')
    plt.xlabel("Athletes")
    plt.ylabel("Points")
    plt.title("Points Scored by Active Players")
    plt.xticks(rotation = 45)
    plt.tight_layout()
    plt.show()

def mainfunct():
    Athletes = participant_names()
    Points = participant_points(Athletes)
    bar_chart(Athletes, Points)

if __name__ == "__main__":
    mainfunct()