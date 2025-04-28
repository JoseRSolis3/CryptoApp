import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QFont

def variables():
    title = "Crypto App"
    geometry = (100, 100, 500, 300)
    label_text = "This is a label"
    button_text = ""
    return title, geometry, label_text, button_text

class Window:
    def __init__(self, title, geometry, label_text, button_text):
        self.window_setup(title, geometry)
    
        self.win_title()
        self.win_geometry()

        self.win_components(label_text, button_text)

        self.window.show()
        sys.exit(self.app.exec_())

    def window_setup(self, title, geometry):
        self.window_title = title
        self.geometry = geometry
        self.app = self.create_app_obj()
        self.window = self.create_window()

    def login_menu(self, title, geometry):
        self.window_setup(title, geometry)

        self.login_layout = self.win_layout()
        header = self.win_label(label_text = "This is a header")
        user = self.win_label(label_text= "username")
        self.login_layout.addWidget(header)

        self.window.setLayout(self.login_layout)

    def create_app_obj(self):
        return QApplication(sys.argv)
    
    def win_layout(self):
        return QVBoxLayout()
    
    def create_window(self):
        return QWidget()

    def win_title(self):
        self.window.setWindowTitle(self.window_title)

    def win_geometry(self):
        self.window.setGeometry(*self.geometry)

    def win_components(self, label_text = None, button_text = None):
        if label_text:
            for text in label_text:
                self.win_label(text)
        
        if button_text:
            for text in button_text:
                self.win_button(text)

    def win_label(self, label_text):
        return QLabel(label_text)

    def win_button(self, button_text):
        return QPushButton(button_text)
    
    def win_entry(self):
        return QLineEdit()
    
class Font():
    def __init__(self):
       self.font = self.font_obj()

    def font_obj(self):
        return QFont()
    
    def font_family(self, font_family):
        self.font.setFamily(font_family)
        return self
    
    def header_1(self):
        self.font.setPointSize(32)
        return self
    
    def header_2(self):
        self.font.setPointSize(24)
        return self
    
    def header_3(self):
        self.font.setPointSize(18)
        return self

    def normal_text(self):
        self.font.setPointSize(14)
        return self
    
    def caption(self):
        self.font.setPointSize(10)
        return self
        

Window(*variables())

# TODO:
# 1. Allow custom labels (already started)
# 2. Allow custom buttons (DONE)
# 3. Add custom entry fields (QLineEdit)
# 4. Allow setting custom geometry dynamically
# 5. Allow setting custom window title dynamically
# 6. Add layout to window (self.window.setLayout(self.layout))
# 7. Style buttons and labels (using setStyleSheet)
# 8. Connect button clicks to functions (slots/signals)
# 9. Organize code into smaller helper functions (optional cleanup)
# 10. Create a simple homepage layout (Label + Button + Entry field)
