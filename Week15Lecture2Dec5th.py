'''
 Name: Connor Kouznetsov
 Description: Week 15 Lecture 2
'''

#Learning GUI's Continued

import tkinter as tk
import tkinter.messagebox

class yardConvert:
    def __init__(self):
        #Creating the Main Window
        self.mw = tk.Tk()
        self.mw.title("Miles to Yards Conversion")


        #Creating the Frames
        self.top = tk.Frame()   #'''self.mw, borderwidth = 5, relief = "sunken", bg = "orange". width = 50, height = 50'''
        self.bottom = tk.Frame()    #'''self.mw, borderwidth = 5, relief = "sunken", bg = "green". width = 50, height = 50'''

        #Creating the Top Frame Widgets
        self.prompt = tk.Label(self.top, text = "Enter the distance i miles:", font = ("Times New Roman Bold", 20))
        self.mentry = tk.Entry(self.top, width = 25)

        #Pack the Top Frame Widgets
        self.prompt.pack(side = "left")
        self.mentry.pack(side = "left")

        #Creating the Bottom Frame Widgets
        self.conv = tk.Button(self.bottom, text = "Convert", command = self.convert, bg = "red", fg = "black", font = ("Arial Bold", 20))
        self.clr = tk.Button(self.bottom, text = "Clear", command = self.clear, bg = "red", fg = "black", font = ("Arial Bold", 20))
        self.quit = tk.Button(self.bottom, text = "Quit", command = self.mw.destroy, bg = "red", fg = "black", font = ("Arial Bold", 20))
        
        #Pack the Button Frame Widgets
        self.conv.pack(side = "left")
        self.clr.pack(side = "left")
        self.quit.pack(side = "left")
    
        #Pack the Frames
        self.top.pack()
        self.bottom.pack()
        
        tk.mainloop()

    def convert(self):
        try:
            mile = float(self.mentry.get())
            yard = mile * 1760

        except ValueError:
            tkinter.messagebox.showinfo("Error", "Please enter a valid number")

        else: 
            tkinter.messagebox.showinfo("Results", f"{mile} miles is {yard:.1f} yards.")
    
    def clear(self):
        self.mentry.delete(0, tk.END)

#End of our Class


#Create Object
cobj = yardConvert()