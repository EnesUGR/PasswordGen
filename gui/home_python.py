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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QToolButton,
    QVBoxLayout, QWidget)

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

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PasswordGen", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"P A S S W O R D", None))
        self.toolButton_copy.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButton_generatePassword.setText(QCoreApplication.translate("MainWindow", u"Generate Password", None))
        self.pushButton_check.setText(QCoreApplication.translate("MainWindow", u"Check Password", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi
