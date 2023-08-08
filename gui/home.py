# pyside6-uic .\home.ui -o .\home_python.py
import sys
from PySide6.QtWidgets import QApplication,QMainWindow
from gui.home_python import Ui_MainWindow
from generating_password import generate_password

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_generatePassword.clicked.connect(self.generate)
        self.ui.toolButton_copy.clicked.connect(self.copy_password)
        self.ui.pushButton_check.clicked.connect(self.check)

    def copy_password(self):
        self.ui.lineEdit_password.selectAll()
        self.ui.lineEdit_password.copy()
        self.ui.lineEdit_password.deselect()

    def generate(self):
        p = generate_password(8, True, True, True, True)
        self.ui.lineEdit_password.setText(p)

    def check(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_check)




def run_ui():
    app = QApplication([])
    win = Home()
    win.show()
    sys.exit(app.exec())