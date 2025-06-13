#ENSURE TO IMPORT TKINTER
import tkinter as tk

from tkinter import messagebox

root = tk.Tk()
root.title("Title")
root.geometry("400x50")

def Greeting():
    
    name_entry = input()

    try: 
        name = name_entry.get().strip()

        if not name:
            raise ValueError("Name cannot be empty.")

    except ValueError as e:
        messagebox.showwarning("Input Error", str(e))
    
    else:
        messagebox.showinfo("Greting", f"Hello, {name}!")

    finally:
        name_entry.delete(1, tk.END)

#root2 = tk.Tk()
#root2.title("Second Window")
#root2.geometry("500x300")

label = tk.Label(root, text = "Please Enter your name")
label.pack(pady = 10)

name_entry = tk.Entry(root)
name_entry.pack(pady = 10)

button = tk.Button(root, text = "Submit", command = Greeting)
button.pack(pady = 5)

greeting = Greeting()