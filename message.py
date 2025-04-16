import tkinter as tk
import json
from pathlib import Path
from utils import read_json

def error_msg():
    path = Path("messages.json")
    data = read_json(path)
    
    return {
        "user_exists": lambda: data["error"]["registration"]["user_exists"],
        "blank_input": lambda: data["error"]["response"]["blank_input"],
        "wrong_password": lambda: data["error"]["login"]["wrong_password"],
        "not_registered": lambda: data["error"]["login"]["user_not_registered"],
    }

#styles the text color green for successes
def get_style():
    styles = {
        "success": {"fg": "green"},
        "error": {"fg": "red"}
    }
    return styles

errors = error_msg()

def clear_msg(frame):
    tk.Label(frame, text="").pack()

def empty_input(frame):
    tk.Label(frame, text=errors["blank_input"](), **get_style()["error"]).pack()

def u_exists(frame):
    tk.Label(frame, text=errors["user_exists"](), **get_style()["error"]).pack()

def wrong_pass(frame):
    tk.Label(frame, text=errors["wrong_password"](), **get_style()["error"]).pack()

def no_registration(frame):
    tk.Label(frame, text=errors["not_registered"](), **get_style()["error"]).pack()
