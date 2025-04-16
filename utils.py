import json
import tkinter as tk

def read_json(path):
    with open(path, "r") as f:
        return json.load(f)
    
def custom_popup(title, message, buttons):
    win = tk.Toplevel()
    win.title(title)
    win.geometry("300x150")
    win.resizable(False, False)

    tk.Label(win, text=message).pack()

    button_frame = tk.Frame(win)
    button_frame.pack()

    for text, command in buttons.items():
        tk.Button(button_frame, text=text, command= lambda c=command: (c(), win.destroy())).pack()

def registration_popup():

    def on_yes():
        print("pressed yes")
    
    def on_no():
        print("pressed no")

    t = "Registration"
    m = "User not found!\nWould you like to register?"

    custom_popup(t, m, {"Yes": on_yes, "No": on_no})