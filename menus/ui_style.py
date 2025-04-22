import tkinter as tk

print("Loading UI Style")
class IUStyle:
    def __init__(self):
        print("Loading Default Label style")
        self.default_label = {
                "font": ("Arial", 14),
                "bg": "white",
                "fg": "black",
                "padx": 10,
                "pady": 5
            }

        print("Loadin default Button style")
        self.default_button = {
                "font": ("Arial", 14),
                "bg": "white",
                "fg": "black",
                "padx": 10,
                "pady": 5
            }

        print("Loading default Entry style")
        self.default_entry = {
                "bg": "white",
                "fg": "black",
                "padx": 5,
                "pady": 2
            }

    print("Applying default Label style")
    def apply_label_style(self, label, overrides=None):
        label_style = self.default_label.copy()
        if overrides:
            label_style.update(overrides)
        label.config(**label_style)

    print("Applying default Button style")
    def apply_button_style(self, button, overrides=None):
        button_style = self.default_button.copy()
        if overrides:
            button_style.update(overrides)
        button.config(**button_style)

    print("Applying default Entry style")
    def apply_entry_style(self, entry, overrides=None):
        entry_style = self.default_entry.copy()
        if overrides:
            entry_style.update(overrides)
        entry.config(**entry_style)

    print("applying default Window style")
    def default_win(self, root, overrides):
        root.title("Crypto App")
        root.geometry("500x300")
        if overrides:
            for key, value in overrides.items():
                getattr(root, key)(value)