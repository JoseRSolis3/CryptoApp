import tkinter as tk
from ui import login_form

def app_window(root):
    root.title("Crypto")
    root.geometry("400x300")
    return root

def main():
    root = tk.Tk()
    app_window(root)

    #calls the login form from ui to pass root as an arguemnt
    login_form(root)

    root.mainloop()

if __name__ == "__main__":
    main()