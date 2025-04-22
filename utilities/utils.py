import tkinter as tk
from menus.ui_style import UIStyle
from menus.ui import creating_window

print("pulling the value of root")
root = creating_window()

def create_instance(entry, overrides):
    ui_style = UIStyle()
    print("applying styles to the entry")
    ui_style.apply_entry_style(entry, overrides)

def username_input(entry, overrides):
    print("Creating Entry widget")
    entry = tk.Entry(root)
    create_instance(entry, overrides)
    print("redefining the value of tk.Entry to default style")
    return entry 