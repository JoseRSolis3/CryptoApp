import tkinter as tk
from menus.ui import login_form

#Designs the Window
def app_window(root):
    root.title("Crypto")
    root.geometry("400x300")

def main():
    # Creates application window
    root = tk.Tk()
    app_window(root)

    #calls the login form from ui to pass root as an argument
    login_form(root)

    #Launches the application
    root.mainloop()

if __name__ == "__main__":
    main()