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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(524, 599)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
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
        self.lineEdit_password.setAlignment(Qt.AlignCenter)
        self.lineEdit_password.setReadOnly(True)

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

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 524, 22))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PasswordGen", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"P A S S W O R D", None))
        self.toolButton_copy.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButton_generatePassword.setText(QCoreApplication.translate("MainWindow", u"Generate Password", None))
        self.pushButton_check.setText(QCoreApplication.translate("MainWindow", u"Check Password", None))
        self.labelChecking_password.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
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
        self.labelChecking_chars.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_gohome.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

