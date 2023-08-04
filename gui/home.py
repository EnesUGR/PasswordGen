# pyside6-uic .\home.ui -o .\home_python.py
import sys
from PySide6.QtWidgets import QApplication,QMainWindow
from gui.home_python import Ui_MainWindow

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



def run_ui():
    app = QApplication([])
    win = Home()
    win.show()
    sys.exit(app.exec())