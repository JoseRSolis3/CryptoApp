import sys
from PyQt5.QtWidgets import QApplication, QWidget

title = "Crypto App"
geometry = (100, 100, 500, 300)

class Window:
    def __init__(self, title, geometry):
        self.window_title = title
        self.geometry = geometry
        self.app = self.create_app_obj()
        self.window = self.create_window()

        self.win_title()
        self.win_geometry()

        self.window.show()
        sys.exit(self.app.exec_())

    def create_app_obj(self):
        return QApplication(sys.argv)
        
    def create_window(self):
        return QWidget()

    def win_title(self):
        self.window.setWindowTitle(self.window_title)

    def win_geometry(self):
        self.window.setGeometry(*geometry)
    
Window(title, geometry)

