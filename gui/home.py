# pyside6-uic .\home.ui -o .\home_python.py
import sys
from PySide6.QtWidgets import QApplication,QMainWindow,QCheckBox
from gui.home_python import Ui_MainWindow
from generating_password import generate_password
from checking_password import Checking
from gui.settings import Settings

class Home(QMainWindow):
    def __init__(self,appname:str):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.settings = Settings(appname)
        self.ui.setupUi(self)
        self.setupUi()
        if self.settings.isEmpty: self.save_settings()

        self.ui.pushButton_generatePassword.clicked.connect(self.generate)
        self.ui.toolButton_copy.clicked.connect(self.copy_password)
        self.ui.pushButton_check.clicked.connect(self.check)
        self.ui.actionHome.triggered.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.page_home))
        self.ui.pushButton_gohome.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.page_home))
        self.ui.actionSettings.triggered.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings))
        self.ui.pushButton_save.clicked.connect(self.save_settings)
        self.ui.toolButton_reset.clicked.connect(lambda : self.setupUi(reset=True))


    def copy_password(self):
        self.ui.lineEdit_password.selectAll()
        self.ui.lineEdit_password.copy()
        self.ui.lineEdit_password.deselect()
        self.ui.statusbar.showMessage("Successfull!",1000)


    def generate(self):
        pgo = self.settings.getSettings["pgo"]
        p = generate_password(pgo["length"], pgo["AZ"], pgo["az_"], pgo["nu"], pgo["sc"])
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
        def diff_color():
            if pcp["strengthC"] <= float(self.ui.labelChecking_score.text()): self.ui.labelChecking_score.setStyleSheet("color: green;")
            else: self.ui.labelChecking_score.setStyleSheet("color: red;")
            if pcp["eabitC"] <= float(self.ui.labelChecking_eabits.text()): self.ui.labelChecking_eabits.setStyleSheet("color: green;")
            else: self.ui.labelChecking_eabits.setStyleSheet("color: red;")
            if pcp["upperC"] <= float(self.ui.labelChecking_uppercase.text()): self.ui.labelChecking_uppercase.setStyleSheet("color: green;")
            else: self.ui.labelChecking_uppercase.setStyleSheet("color: red;")
            if pcp["numbersC"] <= float(self.ui.labelChecking_nums.text()): self.ui.labelChecking_nums.setStyleSheet("color: green;")
            else: self.ui.labelChecking_nums.setStyleSheet("color: red;")
            if pcp["specialC"] <= float(self.ui.labelChecking_specialcase.text()): self.ui.labelChecking_specialcase.setStyleSheet("color: green;")
            else: self.ui.labelChecking_specialcase.setStyleSheet("color: red;")
            if 0.2 > float(self.ui.labelChecking_weakFactor.text()): self.ui.labelChecking_weakFactor.setStyleSheet("color: green;")
            else: self.ui.labelChecking_weakFactor.setStyleSheet("color: red;")
            if ch.get_result():self.ui.labelChecking_password.setStyleSheet("color: #073f0b;")
            else:self.ui.labelChecking_password.setStyleSheet("color: #8d5501;")
        diff_color()


    def setupUi(self,reset=False):
        pgo = self.settings.getSettings["pgo"]
        pcp = self.settings.getSettings["pcp"]

        # generation
        self.ui.checkBox_AZ.setChecked(True if reset else pgo["AZ"])
        self.ui.checkBox_az.setChecked(True if reset else pgo["az_"])
        self.ui.checkBox_09.setChecked(True if reset else pgo["nu"])
        self.ui.checkBox_SpecialChars.setChecked(True if reset else pgo["sc"])
        self.ui.spinBox_length.setValue(8 if reset else pgo["length"])
        # policy
        self.ui.spinBox_checkLength.setValue(8 if reset else pcp["length"])
        self.ui.spinBox_checkUppercase.setValue(2 if reset else pcp["upperC"])
        self.ui.spinBox_checkNumbers.setValue(2 if reset else pcp["numbersC"])
        self.ui.spinBox_checkSpecial.setValue(2 if reset else pcp["specialC"])
        self.ui.spinBox_checkEntropybits.setValue(30 if reset else pcp["eabitC"])
        self.ui.spinBox_checkScore.setValue(0.66 if reset else pcp["strengthC"])
        # settings
        self.save_settings()
        self.set_tool_tips()
        #checkbox changed
        def changed():
            for cb in cs:
                if cb.objectName() == "checkBox_AZ" or cb.objectName() == "checkBox_az" or cb.objectName() == "checkBox_09":
                    if cb.isChecked(): return None
                    else: continue
            self.ui.statusbar.showMessage("You must choose at least one of the first three options.", 3000)
            self.ui.checkBox_AZ.setChecked(True) #Default

        cs:list[QCheckBox] = self.ui.groupBox_1.findChildren(QCheckBox)
        for c in cs: c.clicked.connect(changed)


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


    def save_settings(self):
        self.settings.saveSettings(self.ui.checkBox_AZ.isChecked(),self.ui.checkBox_az.isChecked(),self.ui.checkBox_09.isChecked(),
                                   self.ui.checkBox_SpecialChars.isChecked(),self.ui.spinBox_length.value(),
                                   self.ui.spinBox_checkLength.value(),self.ui.spinBox_checkUppercase.value(),
                                   self.ui.spinBox_checkNumbers.value(),self.ui.spinBox_checkSpecial.value(),
                                   self.ui.spinBox_checkEntropybits.value(),self.ui.spinBox_checkScore.value())
        if self.ui.labelChecking_password.text() != "PASSWORD": self.ui.statusbar.showMessage("Successfull!",2000)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)





def run_ui(appname:str):
    app = QApplication([])
    win = Home(appname)
    win.show()
    sys.exit(app.exec())


def format_large_number(number:int) -> str:
    suffixes = ["", "K", "M", "B", "T"] #Thousand ,Million ,Billion ,Trillion
    for suffix in suffixes:
        if abs(number) < 1000:
            return f"{number:.2f}{suffix}"
        number /= 1000
    return f"{number:.2f}{suffixes[-1]}"