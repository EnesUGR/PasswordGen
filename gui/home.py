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
        self.set_tool_tips()
        self.ui.pushButton_generatePassword.clicked.connect(self.generate)
        self.ui.toolButton_copy.clicked.connect(self.copy_password)
        self.ui.pushButton_check.clicked.connect(self.check)
        self.ui.pushButton_gohome.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.page_home))

    def copy_password(self):
        self.ui.lineEdit_password.selectAll()
        self.ui.lineEdit_password.copy()
        self.ui.lineEdit_password.deselect()

    def generate(self):
        p = generate_password(18, True, True, True, True)
        self.ui.lineEdit_password.setText(p)

    def check(self):
        pw = self.ui.lineEdit_password.text()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_check)

        if pw == "": return None

        ch = Checking(password_text=pw)
        ch_details = ch.get_detailes()
        self.ui.labelChecking_password.setText(pw)
        self.ui.labelChecking_score.setText(ch_details["score"])
        self.ui.labelChecking_eabits.setText(ch_details["eabits"])
        self.ui.labelChecking_weakFactor.setText(str(round(float(ch_details["weak"]),5)))
        self.ui.labelChecking_length.setText(ch_details["length"])
        self.ui.labelChecking_letters.setText(ch_details["letters"])
        self.ui.labelChecking_uppercase.setText(ch_details["uppercase"])
        self.ui.labelChecking_lowercase.setText(ch_details["lowercase"])
        self.ui.labelChecking_specialcase.setText(ch_details["specialcase"])
        self.ui.labelChecking_nums.setText(ch_details["nums"])
        self.ui.labelChecking_repeated.setText(ch_details["repeatedpattern"])
        chars_str = ""
        for key,value in ch_details["chars"].items(): chars_str += f"{key}: {value}\n"
        self.ui.labelChecking_chars.setText(chars_str)
        self.ui.labelChecking_combs.setText(format_large_number(int(ch_details["combs"])))
        self.ui.labelChecking_combs.setToolTip(ch_details["combs"])
        #score color
        if float(ch_details["score"]) >= 0.66:
            self.ui.labelChecking_score.setStyleSheet("color: green;")
        elif float(ch_details["score"]) >= 0.5:
            self.ui.labelChecking_score.setStyleSheet("color: yellow;")
        else:
            self.ui.labelChecking_score.setStyleSheet("color: red;")

    def set_tool_tips(self):
        self.ui.labelChecking_score.setToolTip('An even better, more intuitive test, is to require the password to be "complex enough". Complexity is a number in the range of 0.00..0.99. Good, strong passwords start at 0.66.')
        self.ui.label_1.setToolTip('An even better, more intuitive test, is to require the password to be "complex enough". Complexity is a number in the range of 0.00..0.99. Good, strong passwords start at 0.66.')
        self.ui.labelChecking_eabits.setToolTip("That's how many bits you need to store its alphabet. However, a password that uses plenty of characters has more entropy.")
        self.ui.label_3.setToolTip("That's how many bits you need to store its alphabet. However, a password that uses plenty of characters has more entropy.")
        self.ui.labelChecking_weakFactor.setToolTip("""Get weakness factor as a float in range {0 .. 1}. This detects the portion of the string that contains:\n\t-repeated patterns\n\t-sequences\nE.g. a value of 1.0 means the whole string is weak, and 0.5 means half of the string is weak.""")
        self.ui.label_4.setToolTip("""Get weakness factor as a float in range {0 .. 1}. This detects the portion of the string that contains:\n\t-repeated patterns\n\t-sequences\nE.g. a value of 1.0 means the whole string is weak, and 0.5 means half of the string is weak.""")
        self.ui.labelChecking_repeated.setToolTip("Repeating characters reduce the strength of the password.")
        self.ui.label_10.setToolTip("Repeating characters reduce the strength of the password.")
        self.ui.labelChecking_combs.setToolTip('The number of possible combinations with the current alphabet')
        self.ui.label_11.setToolTip('The number of possible combinations with the current alphabet')
        self.ui.labelChecking_chars.setToolTip("""Character count per top-level category. The following top-level categories are defined\nL: letter\nM: Mark\nN: Number\nP: Punctuation\nS: Symbol\nZ: Separator\nC: Other""")
        self.ui.label_12.setToolTip("""Character count per top-level category. The following top-level categories are defined\nL: letter\nM: Mark\nN: Number\nP: Punctuation\nS: Symbol\nZ: Separator\nC: Other""")




def run_ui():
    app = QApplication([])
    win = Home()
    win.show()
    sys.exit(app.exec())


def format_large_number(number:int) -> str:
    suffixes = ["", "K", "M", "B", "T"]
    for suffix in suffixes:
        if abs(number) < 1000:
            return f"{number:.2f}{suffix}"
        number /= 1000
    return f"{number:.2f}{suffixes[-1]}"