# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QDoubleSpinBox,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QStatusBar, QToolButton,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(545, 599)
        icon = QIcon()
        icon.addFile(u":/icon/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionHome = QAction(MainWindow)
        self.actionHome.setObjectName(u"actionHome")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionSelectTheme = QAction(MainWindow)
        self.actionSelectTheme.setObjectName(u"actionSelectTheme")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_2 = QVBoxLayout(self.page_home)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_password = QLineEdit(self.page_home)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setMinimumSize(QSize(0, 60))
        font = QFont()
        font.setPointSize(12)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setCursor(QCursor(Qt.ArrowCursor))
        self.lineEdit_password.setStyleSheet(u"")
        self.lineEdit_password.setFrame(True)
        self.lineEdit_password.setCursorPosition(0)
        self.lineEdit_password.setAlignment(Qt.AlignCenter)
        self.lineEdit_password.setReadOnly(False)
        self.lineEdit_password.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_password)

        self.toolButton_copy = QToolButton(self.page_home)
        self.toolButton_copy.setObjectName(u"toolButton_copy")
        self.toolButton_copy.setMinimumSize(QSize(30, 60))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setItalic(True)
        self.toolButton_copy.setFont(font1)

        self.horizontalLayout_2.addWidget(self.toolButton_copy)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 20, -1, -1)
        self.toolButton_toFile = QToolButton(self.page_home)
        self.toolButton_toFile.setObjectName(u"toolButton_toFile")
        self.toolButton_toFile.setEnabled(True)
        self.toolButton_toFile.setMinimumSize(QSize(0, 30))
        self.toolButton_toFile.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.toolButton_toFile)

        self.lineEdit_toFilePath = QLineEdit(self.page_home)
        self.lineEdit_toFilePath.setObjectName(u"lineEdit_toFilePath")
        self.lineEdit_toFilePath.setEnabled(True)
        self.lineEdit_toFilePath.setMinimumSize(QSize(0, 30))
        self.lineEdit_toFilePath.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.lineEdit_toFilePath)

        self.spinBox_toFileAmount = QSpinBox(self.page_home)
        self.spinBox_toFileAmount.setObjectName(u"spinBox_toFileAmount")
        self.spinBox_toFileAmount.setMinimumSize(QSize(0, 30))
        self.spinBox_toFileAmount.setAlignment(Qt.AlignCenter)
        self.spinBox_toFileAmount.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBox_toFileAmount.setMaximum(99)

        self.horizontalLayout_11.addWidget(self.spinBox_toFileAmount)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_generatePassword = QPushButton(self.page_home)
        self.pushButton_generatePassword.setObjectName(u"pushButton_generatePassword")
        self.pushButton_generatePassword.setMinimumSize(QSize(0, 60))
        self.pushButton_generatePassword.setFont(font)
        self.pushButton_generatePassword.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.pushButton_generatePassword)

        self.pushButton_check = QPushButton(self.page_home)
        self.pushButton_check.setObjectName(u"pushButton_check")
        self.pushButton_check.setMinimumSize(QSize(0, 60))
        self.pushButton_check.setFont(font)
        self.pushButton_check.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.pushButton_check)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.stackedWidget.addWidget(self.page_home)
        self.page_check = QWidget()
        self.page_check.setObjectName(u"page_check")
        self.verticalLayout_3 = QVBoxLayout(self.page_check)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.labelChecking_password = QLabel(self.page_check)
        self.labelChecking_password.setObjectName(u"labelChecking_password")
        self.labelChecking_password.setMinimumSize(QSize(0, 10))
        self.labelChecking_password.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.labelChecking_password.setFont(font2)
        self.labelChecking_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.labelChecking_password)

        self.gridLayout_check = QGridLayout()
        self.gridLayout_check.setObjectName(u"gridLayout_check")
        self.label_5 = QLabel(self.page_check)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_check.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_3 = QLabel(self.page_check)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_check.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_6 = QLabel(self.page_check)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_check.addWidget(self.label_6, 2, 1, 1, 1)

        self.label_13 = QLabel(self.page_check)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_check.addWidget(self.label_13, 0, 4, 1, 1)

        self.labelChecking_letters = QLabel(self.page_check)
        self.labelChecking_letters.setObjectName(u"labelChecking_letters")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(False)
        self.labelChecking_letters.setFont(font3)
        self.labelChecking_letters.setAlignment(Qt.AlignCenter)

        self.gridLayout_check.addWidget(self.labelChecking_letters, 3, 0, 1, 1)

        self.label_12 = QLabel(self.page_check)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_check.addWidget(self.label_12, 4, 4, 1, 1)

        self.labelChecking_score = QLabel(self.page_check)
        self.labelChecking_score.setObjectName(u"labelChecking_score")
        self.labelChecking_score.setFont(font3)
        self.labelChecking_score.setAlignment(Qt.AlignCenter)

        self.gridLayout_check.addWidget(self.labelChecking_score, 1, 0, 1, 1)

        self.label_10 = QLabel(self.page_check)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_check.addWidget(self.label_10, 4, 1, 1, 1)

        self.label_8 = QLabel(self.page_check)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_check.addWidget(self.label_8, 2, 4, 1, 1)

        self.label_7 = QLabel(self.page_check)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_check.addWidget(self.label_7, 2, 2, 1, 1)

        self.label_11 = QLabel(self.page_check)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_check.addWidget(self.label_11, 4, 2, 1, 1)

        self.label_4 = QLabel(self.page_check)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_check.addWidget(self.label_4, 0, 2, 1, 1)

        self.label_1 = QLabel(self.page_check)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setFont(font1)
        self.label_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_check.addWidget(self.label_1, 0, 0, 1, 1)

        self.label_9 = QLabel(self.page_check)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_check.addWidget(self.label_9, 4, 0, 1, 1)

        self.labelChecking_nums = QLabel(self.page_check)
        self.labelChecking_nums.setObjectName(u"labelChecking_nums")
        self.labelChecking_nums.setFont(font3)
        self.labelChecking_nums.setAlignment(Qt.AlignCenter)

        self.gridLayout_check.addWidget(self.labelChecking_nums, 5, 0, 1, 1)

        self.labelChecking_eabits = QLabel(self.page_check)
        self.labelChecking_eabits.setObjectName(u"labelChecking_eabits")
        self.labelChecking_eabits.setFont(font3)
        self.labelChecking_eabits.setAlignment(Qt.AlignCenter)

        self.gridLayout_check.addWidget(self.labelChecking_eabits, 1, 1, 1, 1)

        self.labelChecking_weakFactor = QLabel(self.page_check)
        self.labelChecking_weakFactor.setObjectName(u"labelChecking_weakFactor")
        self.labelChecking_weakFactor.setFont(font3)
        self.labelChecking_weakFactor.setAlignment(Qt.AlignCenter)

        self.gridLayout_check.addWidget(self.labelChecking_weakFactor, 1, 2, 1, 1)

        self.labelChecking_length = QLabel(self.page_check)
        self.labelChecking_length.setObjectName(u"labelChecking_length")
        self.labelChecking_length.setFont(font3)
        self.labelChecking_length.setAlignment(Qt.AlignCenter)

        self.gridLayout_check.addWidget(self.labelChecking_length, 1, 4, 1, 1)

        self.labelChecking_uppercase = QLabel(self.page_check)
        self.labelChecking_uppercase.setObjectName(u"labelChecking_uppercase")
        self.labelChecking_uppercase.setFont(font3)
        self.labelChecking_uppercase.setAlignment(Qt.AlignCenter)

        self.gridLayout_check.addWidget(self.labelChecking_uppercase, 3, 1, 1, 1)

        self.labelChecking_lowercase = QLabel(self.page_check)
        self.labelChecking_lowercase.setObjectName(u"labelChecking_lowercase")
        self.labelChecking_lowercase.setFont(font3)
        self.labelChecking_lowercase.setAlignment(Qt.AlignCenter)

        self.gridLayout_check.addWidget(self.labelChecking_lowercase, 3, 2, 1, 1)

        self.labelChecking_specialcase = QLabel(self.page_check)
        self.labelChecking_specialcase.setObjectName(u"labelChecking_specialcase")
        self.labelChecking_specialcase.setFont(font3)
        self.labelChecking_specialcase.setAlignment(Qt.AlignCenter)

        self.gridLayout_check.addWidget(self.labelChecking_specialcase, 3, 4, 1, 1)

        self.labelChecking_repeated = QLabel(self.page_check)
        self.labelChecking_repeated.setObjectName(u"labelChecking_repeated")
        self.labelChecking_repeated.setFont(font3)
        self.labelChecking_repeated.setAlignment(Qt.AlignCenter)

        self.gridLayout_check.addWidget(self.labelChecking_repeated, 5, 1, 1, 1)

        self.labelChecking_combs = QLabel(self.page_check)
        self.labelChecking_combs.setObjectName(u"labelChecking_combs")
        self.labelChecking_combs.setFont(font3)
        self.labelChecking_combs.setAlignment(Qt.AlignCenter)

        self.gridLayout_check.addWidget(self.labelChecking_combs, 5, 2, 1, 1)

        self.labelChecking_chars = QLabel(self.page_check)
        self.labelChecking_chars.setObjectName(u"labelChecking_chars")
        self.labelChecking_chars.setFont(font3)
        self.labelChecking_chars.setAlignment(Qt.AlignCenter)

        self.gridLayout_check.addWidget(self.labelChecking_chars, 5, 4, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_check)

        self.pushButton_gohome = QPushButton(self.page_check)
        self.pushButton_gohome.setObjectName(u"pushButton_gohome")
        self.pushButton_gohome.setMinimumSize(QSize(0, 40))
        self.pushButton_gohome.setFont(font)
        self.pushButton_gohome.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.pushButton_gohome)

        self.stackedWidget.addWidget(self.page_check)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.verticalLayout_7 = QVBoxLayout(self.page_settings)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_1 = QGroupBox(self.page_settings)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.groupBox_1.setFlat(True)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_1)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox_AZ = QCheckBox(self.groupBox_1)
        self.checkBox_AZ.setObjectName(u"checkBox_AZ")
        self.checkBox_AZ.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkBox_AZ)

        self.checkBox_az = QCheckBox(self.groupBox_1)
        self.checkBox_az.setObjectName(u"checkBox_az")
        self.checkBox_az.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkBox_az)

        self.checkBox_09 = QCheckBox(self.groupBox_1)
        self.checkBox_09.setObjectName(u"checkBox_09")
        self.checkBox_09.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkBox_09)

        self.checkBox_SpecialChars = QCheckBox(self.groupBox_1)
        self.checkBox_SpecialChars.setObjectName(u"checkBox_SpecialChars")
        self.checkBox_SpecialChars.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkBox_SpecialChars)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.groupBox_1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2, 0, Qt.AlignLeft)

        self.spinBox_length = QSpinBox(self.groupBox_1)
        self.spinBox_length.setObjectName(u"spinBox_length")
        self.spinBox_length.setMinimum(4)
        self.spinBox_length.setMaximum(100)
        self.spinBox_length.setValue(8)

        self.horizontalLayout_4.addWidget(self.spinBox_length)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.verticalLayout_7.addWidget(self.groupBox_1)

        self.groupBox_2 = QGroupBox(self.page_settings)
        self.groupBox_2.setObjectName(u"groupBox_2")
        font4 = QFont()
        font4.setBold(False)
        self.groupBox_2.setFont(font4)
        self.groupBox_2.setFlat(True)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_5.addWidget(self.label_14)

        self.spinBox_checkLength = QSpinBox(self.groupBox_2)
        self.spinBox_checkLength.setObjectName(u"spinBox_checkLength")
        self.spinBox_checkLength.setMinimum(4)
        self.spinBox_checkLength.setMaximum(50)
        self.spinBox_checkLength.setValue(8)

        self.horizontalLayout_5.addWidget(self.spinBox_checkLength)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_6.addWidget(self.label_15)

        self.spinBox_checkUppercase = QSpinBox(self.groupBox_2)
        self.spinBox_checkUppercase.setObjectName(u"spinBox_checkUppercase")
        self.spinBox_checkUppercase.setMinimum(2)
        self.spinBox_checkUppercase.setMaximum(30)

        self.horizontalLayout_6.addWidget(self.spinBox_checkUppercase)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_7.addWidget(self.label_16)

        self.spinBox_checkNumbers = QSpinBox(self.groupBox_2)
        self.spinBox_checkNumbers.setObjectName(u"spinBox_checkNumbers")
        self.spinBox_checkNumbers.setMinimum(2)
        self.spinBox_checkNumbers.setMaximum(30)

        self.horizontalLayout_7.addWidget(self.spinBox_checkNumbers)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_8.addWidget(self.label_17)

        self.spinBox_checkSpecial = QSpinBox(self.groupBox_2)
        self.spinBox_checkSpecial.setObjectName(u"spinBox_checkSpecial")
        self.spinBox_checkSpecial.setMinimum(2)
        self.spinBox_checkSpecial.setMaximum(30)

        self.horizontalLayout_8.addWidget(self.spinBox_checkSpecial)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_18 = QLabel(self.groupBox_2)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_10.addWidget(self.label_18)

        self.spinBox_checkEntropybits = QSpinBox(self.groupBox_2)
        self.spinBox_checkEntropybits.setObjectName(u"spinBox_checkEntropybits")
        self.spinBox_checkEntropybits.setMinimum(2)
        self.spinBox_checkEntropybits.setMaximum(30)
        self.spinBox_checkEntropybits.setValue(30)

        self.horizontalLayout_10.addWidget(self.spinBox_checkEntropybits)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_19 = QLabel(self.groupBox_2)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_9.addWidget(self.label_19)

        self.spinBox_checkScore = QDoubleSpinBox(self.groupBox_2)
        self.spinBox_checkScore.setObjectName(u"spinBox_checkScore")
        self.spinBox_checkScore.setMaximum(1.000000000000000)
        self.spinBox_checkScore.setSingleStep(0.010000000000000)
        self.spinBox_checkScore.setValue(0.660000000000000)

        self.horizontalLayout_9.addWidget(self.spinBox_checkScore)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.horizontalLayout_bottom = QHBoxLayout()
        self.horizontalLayout_bottom.setObjectName(u"horizontalLayout_bottom")
        self.horizontalLayout_bottom.setContentsMargins(-1, 20, -1, -1)
        self.pushButton_save = QPushButton(self.page_settings)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setMinimumSize(QSize(0, 60))
        self.pushButton_save.setFont(font)
        self.pushButton_save.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_bottom.addWidget(self.pushButton_save)

        self.toolButton_reset = QToolButton(self.page_settings)
        self.toolButton_reset.setObjectName(u"toolButton_reset")
        self.toolButton_reset.setMinimumSize(QSize(30, 60))
        font5 = QFont()
        font5.setItalic(True)
        self.toolButton_reset.setFont(font5)

        self.horizontalLayout_bottom.addWidget(self.toolButton_reset)


        self.verticalLayout_7.addLayout(self.horizontalLayout_bottom)

        self.stackedWidget.addWidget(self.page_settings)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 545, 22))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionSelectTheme)
        self.menuMenu.addAction(self.actionHome)
        self.menuMenu.addAction(self.actionSettings)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionAbout)
        self.menuMenu.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PasswordGen", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(shortcut)
        self.actionSettings.setShortcut(QCoreApplication.translate("MainWindow", u"F2", None))
#endif // QT_CONFIG(shortcut)
        self.actionHome.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(shortcut)
        self.actionHome.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionSelectTheme.setText(QCoreApplication.translate("MainWindow", u"Select Theme...", None))
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"P A S S W O R D", None))
#if QT_CONFIG(tooltip)
        self.toolButton_copy.setToolTip(QCoreApplication.translate("MainWindow", u"Copy password (Press Ctrl+C)", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_copy.setText(QCoreApplication.translate("MainWindow", u"C", None))
#if QT_CONFIG(shortcut)
        self.toolButton_copy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.toolButton_toFile.setText(QCoreApplication.translate("MainWindow", u"Save to File", None))
#if QT_CONFIG(tooltip)
        self.spinBox_toFileAmount.setToolTip(QCoreApplication.translate("MainWindow", u"Maximum: 99", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_generatePassword.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>(Press Enter)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_generatePassword.setText(QCoreApplication.translate("MainWindow", u"Generate Password", None))
#if QT_CONFIG(shortcut)
        self.pushButton_generatePassword.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButton_check.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>(Press Shift+Enter)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_check.setText(QCoreApplication.translate("MainWindow", u"Check Password", None))
#if QT_CONFIG(shortcut)
        self.pushButton_check.setShortcut(QCoreApplication.translate("MainWindow", u"Shift+Return", None))
#endif // QT_CONFIG(shortcut)
        self.labelChecking_password.setText(QCoreApplication.translate("MainWindow", u"PASSWORD", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Letters", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Entropybits", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Uppercases", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Length", None))
        self.labelChecking_letters.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Chars", None))
        self.labelChecking_score.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Repeated\n"
"Patterns", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Specialcases", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Lowecases", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Combinations", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Weak Factor", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Score", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Numbers", None))
        self.labelChecking_nums.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.labelChecking_eabits.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.labelChecking_weakFactor.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.labelChecking_length.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.labelChecking_uppercase.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.labelChecking_lowercase.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.labelChecking_specialcase.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.labelChecking_repeated.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.labelChecking_combs.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.labelChecking_chars.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.pushButton_gohome.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("MainWindow", u"Password Generate Options", None))
        self.checkBox_AZ.setText(QCoreApplication.translate("MainWindow", u"A-Z", None))
        self.checkBox_az.setText(QCoreApplication.translate("MainWindow", u"a-z", None))
        self.checkBox_09.setText(QCoreApplication.translate("MainWindow", u"0-9", None))
        self.checkBox_SpecialChars.setText(QCoreApplication.translate("MainWindow", u"Special Chars", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Length:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Password Check Policy", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Length:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Uppercase", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Numbers:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Special Char:", None))
#if QT_CONFIG(tooltip)
        self.label_18.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Entropy bits are a concept that defines how diverse your password has.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Entropybits:", None))
#if QT_CONFIG(whatsthis)
        self.spinBox_checkEntropybits.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.label_19.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Entropy bits are important, but difficult to understand. An even better, more intuitive test is to require the password to be &quot;complex enough&quot;. Complexity is a number in the range of 0.00..0.99. Good, strong passwords start at 0.66.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Strength:", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(tooltip)
        self.toolButton_reset.setToolTip(QCoreApplication.translate("MainWindow", u"Reset to default (Press R)", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_reset.setText(QCoreApplication.translate("MainWindow", u"R", None))
#if QT_CONFIG(shortcut)
        self.toolButton_reset.setShortcut(QCoreApplication.translate("MainWindow", u"R", None))
#endif // QT_CONFIG(shortcut)
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

