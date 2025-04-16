import tkinter as tk
from ui import login_form

def app_window():
    root = tk.Tk()
    root.title("Cypto")
    root.geometry("400x300")
    return root

def main():

    root = app_window()

    #calls the login form from ui to pass root as an arguemnt
    login_form(root)

    root.mainloop()

if __name__ == "__main__":
    main()