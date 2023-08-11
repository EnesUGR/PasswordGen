# pyside6-uic .\home.ui -o .\home_python.py
import sys
from PySide6.QtWidgets import QApplication,QMainWindow
from gui.home_python import Ui_MainWindow
from generating_password import generate_password
from checking_password import Checking
from gui.settings import Settings

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.settings = Settings()
        self.ui.setupUi(self)
        self.set_tool_tips()
        self.save_settings()
        self.ui.pushButton_generatePassword.clicked.connect(self.generate)
        self.ui.toolButton_copy.clicked.connect(self.copy_password)
        self.ui.pushButton_check.clicked.connect(self.check)
        self.ui.actionHome.triggered.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.page_home))
        self.ui.pushButton_gohome.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.page_home))
        self.ui.actionSettings.triggered.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings))
        self.ui.pushButton_save.clicked.connect(self.save_settings)
        self.ui.toolButton_reset.clicked.connect(self.reset_default)

    def copy_password(self):
        self.ui.lineEdit_password.selectAll()
        self.ui.lineEdit_password.copy()
        self.ui.lineEdit_password.deselect()

    def generate(self):
        pgo = self.settings.getSettings["pgo"]
        p = generate_password(pgo["length"], pgo["AZ"], pgo["az"], pgo["nu"], pgo["sc"])
        self.ui.lineEdit_password.setText(p)

    def check(self):
        pw = self.ui.lineEdit_password.text()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_check)

        if pw == "": return None

        pcp: dict = self.settings.getSettings["pcp"]
        ch = Checking(password_text=pw,length=pcp["length"],uppercase=pcp["upperC"],numbers=pcp["numbersC"],
                      special=pcp["specialC"],entropybits=pcp["eabitC"],strength=pcp["strengthC"])
        ch_details = ch.get_detailes()
        def set_text():
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
        set_text()

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

    def reset_default(self):
        #generation
        self.ui.checkBox_AZ.setChecked(True)
        self.ui.checkBox_az.setChecked(True)
        self.ui.checkBox_09.setChecked(True)
        self.ui.checkBox_SpecialChars.setChecked(True)
        self.ui.spinBox_length.setValue(8)
        #policy
        self.ui.spinBox_checkLength.setValue(8)
        self.ui.spinBox_checkUppercase.setValue(2)
        self.ui.spinBox_checkNumbers.setValue(2)
        self.ui.spinBox_checkSpecial.setValue(2)
        self.ui.spinBox_checkEntropybits.setValue(30)
        self.ui.spinBox_checkScore.setValue(0.66)

    def save_settings(self):
        self.settings.saveSettings(self.ui.checkBox_AZ.isChecked(),self.ui.checkBox_az.isChecked(),self.ui.checkBox_09.isChecked(),
                                   self.ui.checkBox_SpecialChars.isChecked(),self.ui.spinBox_length.value(),
                                   self.ui.spinBox_checkLength.value(),self.ui.spinBox_checkUppercase.value(),
                                   self.ui.spinBox_checkNumbers.value(),self.ui.spinBox_checkSpecial.value(),
                                   self.ui.spinBox_checkEntropybits.value(),self.ui.spinBox_checkScore.value())
        if self.ui.labelChecking_password.text() != "PASSWORD": self.ui.statusbar.showMessage("Successfull!",2000)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)





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