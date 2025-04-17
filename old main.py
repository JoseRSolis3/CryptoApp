import tkinter as tk
from menus.ui import login_form, create_error_label

def main():

import json
from pathlib import Path



def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

root = tk.Tk() # tk.Tk() is the actual app
root.title("Crypto") #Title to application window
root.geometry("500x300") #size of application when called

def clear_error(error_label):
    error_label.config(text="")
    return error_label   

def checking_user_existance(username, error_label):
    #creates a link between the py file and the json file
    path = Path("desktop_app_users.json")
    with open(path, "r") as f:
        data = json.load(f)

    path_error = Path("messages.json")
    with open(path_error, "r") as e:
        error_data = json.load(e)

    if not username:
        empty_user_pass = error_data["Error"]['login']["blank"]
        if error_label:
            error_label.config(text=empty_user_pass)
            return True

    #checks if the user is registered
    if username in data["users"]:
        #creates a variable that pulls the error message
        exists = error_data["Error"]["registration"]["user_exists"]
        if error_label:
            #changes the label to an empty one
            error_label.config(text=exists)
        return True
    else:
        return False  

def log_in(username, password, error_label):
    path = Path("desktop_app_users.json")
    with open(path, "r") as f:
        data = json.load(f)

    path_error = Path("messages.json")
    with open(path_error, "r") as e:
        error_data = json.load(e)

    if not username:
        empty_user_pass = error_data["Error"]['login']["blank"]
        if error_label:
            error_label.config(text=empty_user_pass)
            return False
    else:
        password = hash_password(password)
        if password == data["users"][username]["password"]:
            user_home(username)
            return True
        else:
            wrong_pass = error_data["Error"]["login"]["wrong_password"]
            if error_label:
                error_label.config(text=wrong_pass)
            return False        

#register a new user with parameters username and password
def register_user(username, password, error_label):
    alert = Path("messages.json")
    #finds the json file; if it doesn't exist, creates it
    path = Path("desktop_app_users.json")


    #if not in the file...
    if not path.exists():

        #create the file and writes: ({"users": {entered username}}, f, indent=4)
        with open(path, "w") as f:
            json.dump({"users": {}}, f, indent=4)

        #once created json file will look like this:
        #   {
        #       "users":{
        #           // usernames will be added here
        #       }
        #   }

    if checking_user_existance(username,error_label) == True:
        return True

    #then opens and loads the information from the json file
    with open(path, "r") as f:
        data = json.load(f)


    #creates user data within "users" and adds callable variables
    data["users"][username] ={
        "password": hash_password(password),
        "strategies": [],
        "goals": [], 
    }
        #once created json file will look like this:
        #   {
        #       "users":{
        #           username:{
        #               "password": hash_password(password),
        #               "strategies": [],
        #               "goals": [], 
        #           }
        #       }
        #   }

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    with open(alert, "r") as e:
        alert_data = json.load(e)
    
    success = alert_data["success"]["registration"]["user_registered"]

    if error_label:
        error_label.config(text=success)
    return True
              
        

#main menu
def login_menu():
+
    #creates a label to log in
    tk.Label(root, text="Log in:").pack(pady=10)

    #creates a text box for username
    tk.Label(root, text="Username:").pack()
    username = tk.Entry(root)
    username.pack()

    #creates a text box for password
    tk.Label(root, text="Password:").pack()
    password = tk.Entry(root, show="*")
    password.pack()

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)
    
    error_label = tk.Label(root, text="", fg="red")
    error_label.pack()

    def press_enter(event):
        log_in(username.get(), password.get(), error_label)
    
    password.bind('<Return>', press_enter)

    #creates a button and prints the entered information
    tk.Button(
        frame,
        text="Log in",
        command= lambda:
            log_in(username.get(), password.get(), error_label),
        width=15
    ).pack(side="left", pady=5)

    tk.Button(
        frame,
        text="Register",
        command= lambda: [
            clear_error(error_label), 
            register_user(username.get(), password.get(), error_label)
        ],
        width=15
    ).pack(side="left", pady=10)

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def user_home(username):
    clear_window()
    
    welcome = "Welcome back {}!".format(username)
    tk.Label(root, text=welcome).pack()


# Runs the login menu
login_menu()
# Starts the app
root.mainloop()