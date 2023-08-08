# pyside6-uic .\home.ui -o .\home_python.py
import sys
from PySide6.QtWidgets import QApplication,QMainWindow
from gui.home_python import Ui_MainWindow
from generating_password import generate_password
from checking_password import Checking

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_generatePassword.clicked.connect(self.generate)
        self.ui.toolButton_copy.clicked.connect(self.copy_password)
        self.ui.pushButton_check.clicked.connect(self.check)
        self.ui.pushButton_gohome.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.page_home))

    def copy_password(self):
        self.ui.lineEdit_password.selectAll()
        self.ui.lineEdit_password.copy()
        self.ui.lineEdit_password.deselect()

    def generate(self):
        p = generate_password(8, True, True, True, True)
        self.ui.lineEdit_password.setText(p)

    def check(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_check)
        pw = self.ui.lineEdit_password.text()
        ch = Checking(password_text=pw)
        ch_details = ch.get_detailes()
        self.ui.labelChecking_password.setText(pw)
        self.ui.labelChecking_score.setText(ch_details["score"])
        self.ui.labelChecking_eabits.setText(ch_details["eabits"])
        self.ui.labelChecking_weakFactor.setText(ch_details["weak"])
        self.ui.labelChecking_length.setText(ch_details["length"])
        self.ui.labelChecking_letters.setText(ch_details["letters"])
        self.ui.labelChecking_uppercase.setText(ch_details["uppercase"])
        self.ui.labelChecking_lowercase.setText(ch_details["lowercase"])
        self.ui.labelChecking_specialcase.setText(ch_details["specialcase"])
        self.ui.labelChecking_nums.setText(ch_details["nums"])
        self.ui.labelChecking_repeated.setText(ch_details["repeatedpattern"])
        # self.ui.labelChecking_chars.setText(ch_details["chars"])
        self.ui.labelChecking_combs.setText(ch_details["combs"])





def run_ui():
    app = QApplication([])
    win = Home()
    win.show()
    sys.exit(app.exec())