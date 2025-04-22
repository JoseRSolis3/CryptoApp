import tkinter as tk 

def creating_window():
    print("Link start")
    root = tk.Tk()
    print("window created")
    return root

def creating_frame(master=None):
    print("Creating frame")
    frame = tk.Frame(master)
    print('Frame created')
    return frame 

