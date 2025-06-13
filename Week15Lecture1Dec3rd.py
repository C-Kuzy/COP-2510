'''
 Author: Connor Kouznetsov
 Description: Intro to GUI programming
'''
#Part #1
#INTRO TO GUI's - graphical user interfaces
import tkinter as tk

class FirstGUI:
    def __init__(self):
        self.window = tk.Tk() #This creates the window
        self.window.title("My First GUI Widget") #This creates a title for the window

    #END OF PART #1 ---------------------------------------------------------------------------------------------------------------------------------------------------------

        #Part #2: Creating Widgets
        """All other widgets will be below here..."""

        #Label Widget
        self.label = tk.Label(self.window, text = "This is a label.", borderwidth = 200, relief = "groove", bg = "green", fg = "black", font = ("Times New Roman", 25))

        #Pack Label Widget (default is "top": other optioons are "bottom", "left", "right")
        self.label.pack(side = "bottom")

        #Frame Widget
        self.topframe = tk.Frame(self.window, borderwidth = 5, relief = "sunken", bg = "blue", width = 65, height = 65)
        self.bottomframe = tk.Frame(self.window, borderwidth = 5, relief = "groove", bg = "red", width = 75, height = 75)

        #Create a label within a frame
        self.toplabel = tk.Label(self.topframe, text = "Top frame label", borderwidth = 5, relief = "ridge")
        self.bottomlabel = tk.Label(self.bottomframe, text = "Bottom frame label", borderwidth = 5, relief = "raised")

        #Pack Labels within Frames
        self.toplabel.pack(side = "left", ipadx = 30, ipady = 30)
        self.bottomlabel.pack(side = "right", ipadx = 40, ipady = 40)
 
        #Packing Frames
        self.topframe.pack(side = "top", ipadx = 60, ipady = 60)
        self.bottomframe.pack(side = "bottom", ipadx = 75, ipady = 75)

    #END OF PART #2 ---------------------------------------------------------------------------------------------------------------------------------------------------------

    #Part 3 - Button Widget
        #Creating Button Widget
        self.quit = tk.Button(self.window, text = "Quit", command = self.window.destroy, bg = "purple", fg = "gray", font = ("Times New Roman", 20))

        #Pack the Button Widget
        self.quit.pack(side = "bottom", ipadx = 50.50, ipady = 50.50)

    #END OF PART #3 ---------------------------------------------------------------------------------------------------------------------------------------------------------

        #tkinter main loop
        tk.mainloop()

#Driver Portion
firstgui = FirstGUI() #This creates an instance of the class