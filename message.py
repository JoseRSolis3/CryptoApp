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


def messages(frame):

    errors = error_msg()
    
    msg = tk.Label(frame, text="")
    msg.pack()

    def empty_input(frame):
        msg.config(text=errors["blank_input"](), **get_style()["error"])
        msg.pack()
        return msg

    def u_exists(frame):
        msg.config(text=errors["user_exists"](), **get_style()["error"])
        msg.pack()
        return msg

    def wrong_pass(frame):
        msg.config(text=errors["wrong_password"](), **get_style()["error"])
        msg.pack()
        return msg

    def no_registration(frame):
        msg.config(text=errors["not_registered"](), **get_style()["error"])
        msg.pack()
        return msg
    
    return {
        "empty_input": empty_input,
        "user_exists": u_exists,
        "wrong_password": wrong_pass,
        "not_registered": no_registration,
        "widget": msg
    }
