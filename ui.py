import tkinter as tk
from user_management import getting_user_login, user_not_registered
from message import messages

#sets up the main frame based on the root
def framing(root):
    frame = tk.Frame(root)
    frame.pack(pady=20)
    return frame
    
#creates and returns the entry field for username input
def username_entry(frame):
    tk.Label(frame, text="Username:").pack()
    username = tk.Entry(frame)
    username.pack()

    #returns users username input
    return username

#creates and returns the entry field for password input
def password_entry(frame):
    tk.Label(frame, text="Password:").pack()
    password = tk.Entry(frame, show="*")
    password.pack()

    #returns users password entry
    return password


# MAIN MENU -----
def login_form(root):

    #builds the frame
    frame = framing(root)

    #builds the text box for the entry and comes out as data of the entry
    username = username_entry(frame)
    password = password_entry(frame)

    msg = tk.Label(text="")
    msg.pack()

    msgs = messages(msg)

    tk.Button(
        frame,
        text="Login",
        command = lambda:(

            msgs["reset"](),

            #imported from user management, it gets the data from the tk.Entry
            getting_user_login(username, password),

            #checks if user is registered using JSON data (from user_management)
            user_not_registered(*getting_user_login(username, password), msg)
        )
    ).pack()
# ---------------
