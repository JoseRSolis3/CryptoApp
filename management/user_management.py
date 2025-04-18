import tkinter as tk
import json
from pathlib import Path
import hashlib
from alerts.message import messages
from utilities.utils import read_json, clear_window



def open_path():
    return Path("desktop_app_users.json")

def on_login(username, password):
    user, pwd = getting_user_login(username, password)
    user_not_registered(user, pwd)

#Retrieves username and password input from Entry widgests in ui.py
def getting_user_login(username, password):
    return username.get(), password.get()

#hashes the password using SHA-256 encryption
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#Retrieves the "user" dictionary from the JSON data
def getting_data(data):
    return data.get("users", {})

#Adds a new user profile with hashed password and empty strategy/goal lists
def adding_user(path, data, username, password):
    data["users"][username]= {
        "password": hash_password(password),
        "role": "user",
        "strategies": [],
        "goals": [],
    }

    #Writes updated user data to the JSON file
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

#creates a new JSON file with an empty "users" dictionary
def create_file(path):
    with open(path, "w") as f:
        json.dump({"users": {}}, f, indent=4)

#registers the user if they do not already exist
def user_not_registered(username, password,msg):
    
    path = open_path()

    data = read_json(path) 
    existing_users = getting_data(data)    

    msgs = messages(msg)

    #if username input is blank
    if not username:
        msgs["empty_input"]()
        return True
    
    #if the user already exists in the JSON file
    if username in existing_users:
        msgs["user_exists"]()
        return True
    else:
        #Add the new user to the data an save it 
        adding_user(path, data, username, password)

def log_in(username, password, msg, root):
    path = open_path()

    data = read_json(path)
    existing_users = getting_data(data)
    
    msgs = messages(msg)

    password = hash_password(password)

    #if there is no input it runs the empty_input error message
    if not username:
        msgs["empty_input"]()
        return True
    
    #if the username doesnt exists, then activate the registration popup
    #**might change this to stay on the window instead of a popup
    elif username not in existing_users:
        return True
    
    #if the password does not match the user, run the wrong_password error message
    if password != data["users"][username]["password"]:
        msgs["wrong_password"]()
        return True
    
    #if the password is correct, clear the window (personal user window builds in ui.py)
    if password == data["users"][username]["password"]:
        clear_window(root)
        return True

def user_switch():
    return{
        "register" : lambda: adding_user()
    }