import json
import tkinter as tk

# Extracts the information to read
def read_json(path):
    with open(path, "r") as f:
        return json.load(f)
    
# Creates a popup window    
def custom_popup(title, message, buttons):
    #Initiates the popup build
    win = tk.Toplevel()

    #styles the popup
    win.title(title)
    win.geometry("300x150")

    #prevents the user from resizing the window
    win.resizable(False, False)

    #sets up customizable Lable for different functions
    tk.Label(win, text=message).pack()

    #creates a button 
    button_frame = tk.Frame(win)
    button_frame.pack()

    #plugs in values that dev enters as arguments to build the popup
    for text, command in buttons.items():
        tk.Button(button_frame, text=text, command= lambda c=command: (c(win), win.destroy())).pack(side=tk.LEFT)

#Creates the registration popup
def registration_popup():

    def on_yes(win):
        print("pressed yes")
    
    def on_no(win):
        print("pressed no")
        win.destroy()

    t = "Registration"
    m = "User not found!\nWould you like to register?"

    custom_popup(t, m, {"Yes": on_yes, "No": on_no})

#Clears the window
def clear_window(root):
    for widget in root.winfo_children():
        widget.destroy()