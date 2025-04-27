import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

title = "Crypto App"
geometry = (100, 100, 500, 300)
label_text = "This is a label"

class Window:
    def __init__(self, title, geometry, label_text = None, button_text = None):
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
        self.layout = QVBoxLayout()        

    def create_app_obj(self):
        return QApplication(sys.argv)
        
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

    def win_button(self):
        button = QPushButton("Click Me!")
        self.layout.addWidget(button)

Window(title, geometry, label_text)

