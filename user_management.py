import tkinter as tk
import json
from pathlib import Path
import hashlib
from message import messages
from utils import read_json

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
def user_not_registered(username, password, frame):
    
    path = Path("desktop_app_users.json")  

    data = read_json(path)
    existing_users = getting_data(data)    

    msgs = messages(frame)

    #if username input is blank
    if not username:
        msgs["empty_input"](frame)
        print("entry was blank!")
        return True
    
    #if the user already exists in the JSON file
    if username in existing_users:
        print("user exists!")
        return True
    else:
        #Add the new user to the data an save it 
        adding_user(path, data, username, password)