import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit

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

        self.window.setLayout(self.layout)

        self.window.show()
        sys.exit(self.app.exec_())

    def window_setup(self, title, geometry):
        self.window_title = title
        self.geometry = geometry
        self.app = self.create_app_obj()
        self.window = self.create_window()

    def login_menu(self):
        self.login_layout = self.win_layout()
        
        self.login_layout.addWidget()

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
        label = QLabel(label_text)
        self.layout.addWidget(label)

    def win_button(self, button_text):
        button = QPushButton(button_text)
        self.layout.addWidget(button)
    
    def win_entry(self):
        entry = QLineEdit()
        self.layout.addWidget(entry)

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
