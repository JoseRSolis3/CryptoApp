import tkinter as tk
import json
from pathlib import Path
from utils import read_json

def error_msg():
    path = Path("messages.json")
    data = read_json(path)
    
    #sets up specific extraction of data
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


def messages(msg):
    #creates a variable that can extract library content
    errors = error_msg()

    #extracts the blank_input response with get_style
    def empty_input():
        msg.config(text=errors["blank_input"](), **get_style()["error"])
        msg.pack()
        return msg

    #extracts the user_exists response with get_style
    def u_exists():
        msg.config(text=errors["user_exists"](), **get_style()["error"])
        msg.pack()
        return msg

    #extracts the wrong_password response with get_style
    def wrong_pass():
        msg.config(text=errors["wrong_password"](), **get_style()["error"])
        msg.pack()
        return msg

    #extracts the not_registered response with get_style
    def no_registration():
        msg.config(text=errors["not_registered"](), **get_style()["error"])
        msg.pack()
        return msg
    
    #returns the label with a default Label
    def reset():
        msg.config(text="")
        msg.pack()
        return msg
    
    #sets up specific extraction of responses
    return {
        "empty_input": empty_input,
        "user_exists": u_exists,
        "wrong_password": wrong_pass,
        "not_registered": no_registration,
        "reset": reset,
        "widget": msg
    }
