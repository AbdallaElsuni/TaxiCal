# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QWidget)
import Icons.TaxiCal_Icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(616, 422)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Main/T.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.actionNew_Account = QAction(MainWindow)
        self.actionNew_Account.setObjectName(u"actionNew_Account")
        self.actionNew_Account.setCheckable(True)
        self.actionNew_Account.setChecked(True)
        self.actionAccount_1 = QAction(MainWindow)
        self.actionAccount_1.setObjectName(u"actionAccount_1")
        self.actionAccount_1.setCheckable(True)
        self.actionAccount_1.setEnabled(False)
        self.actionAccount_Manager = QAction(MainWindow)
        self.actionAccount_Manager.setObjectName(u"actionAccount_Manager")
        icon1 = QIcon()
        icon1.addFile(u":/Main/Account.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAccount_Manager.setIcon(icon1)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/About.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAbout.setIcon(icon2)
        self.actionUpdate = QAction(MainWindow)
        self.actionUpdate.setObjectName(u"actionUpdate")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout_2 = QFormLayout(self.centralwidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.gb_Name = QGroupBox(self.centralwidget)
        self.gb_Name.setObjectName(u"gb_Name")
        self.gb_Name.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.gb_Name)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_FirstName = QLabel(self.gb_Name)
        self.lb_FirstName.setObjectName(u"lb_FirstName")
        self.lb_FirstName.setFont(font)

        self.horizontalLayout.addWidget(self.lb_FirstName)

        self.le_FirstName = QLineEdit(self.gb_Name)
        self.le_FirstName.setObjectName(u"le_FirstName")

        self.horizontalLayout.addWidget(self.le_FirstName)

        self.lb_LastName = QLabel(self.gb_Name)
        self.lb_LastName.setObjectName(u"lb_LastName")
        self.lb_LastName.setFont(font)

        self.horizontalLayout.addWidget(self.lb_LastName)

        self.le_LastName = QLineEdit(self.gb_Name)
        self.le_LastName.setObjectName(u"le_LastName")

        self.horizontalLayout.addWidget(self.le_LastName)


        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.gb_Name)

        self.gb_IncomeAndStatus = QGroupBox(self.centralwidget)
        self.gb_IncomeAndStatus.setObjectName(u"gb_IncomeAndStatus")
        self.gb_IncomeAndStatus.setFont(font)
        self.formLayout = QFormLayout(self.gb_IncomeAndStatus)
        self.formLayout.setObjectName(u"formLayout")
        self.lb_MaritalStatus = QLabel(self.gb_IncomeAndStatus)
        self.lb_MaritalStatus.setObjectName(u"lb_MaritalStatus")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lb_MaritalStatus)

        self.cb_Status = QComboBox(self.gb_IncomeAndStatus)
        self.cb_Status.addItem("")
        self.cb_Status.addItem("")
        self.cb_Status.addItem("")
        self.cb_Status.addItem("")
        self.cb_Status.setObjectName(u"cb_Status")
        self.cb_Status.setEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cb_Status)

        self.lb_Income = QLabel(self.gb_IncomeAndStatus)
        self.lb_Income.setObjectName(u"lb_Income")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lb_Income)

        self.le_Income = QLineEdit(self.gb_IncomeAndStatus)
        self.le_Income.setObjectName(u"le_Income")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_Income)


        self.formLayout_2.setWidget(1, QFormLayout.SpanningRole, self.gb_IncomeAndStatus)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_Exit = QPushButton(self.groupBox)
        self.pb_Exit.setObjectName(u"pb_Exit")
        self.pb_Exit.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/Buttons/Cross.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Exit.setIcon(icon3)

        self.gridLayout.addWidget(self.pb_Exit, 0, 0, 1, 1)

        self.pb_Submit = QPushButton(self.groupBox)
        self.pb_Submit.setObjectName(u"pb_Submit")
        self.pb_Submit.setEnabled(False)
        self.pb_Submit.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/Buttons/submit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Submit.setIcon(icon4)

        self.gridLayout.addWidget(self.pb_Submit, 0, 1, 1, 1)


        self.formLayout_2.setWidget(2, QFormLayout.SpanningRole, self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_2.setItem(3, QFormLayout.SpanningRole, self.verticalSpacer)

        self.lb_LoginQuestion = QLabel(self.centralwidget)
        self.lb_LoginQuestion.setObjectName(u"lb_LoginQuestion")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(True)
        self.lb_LoginQuestion.setFont(font1)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.lb_LoginQuestion)

        self.pb_Login = QPushButton(self.centralwidget)
        self.pb_Login.setObjectName(u"pb_Login")
        self.pb_Login.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/Buttons/Credentials.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Login.setIcon(icon5)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.pb_Login)

        self.lb_Messege = QLabel(self.centralwidget)
        self.lb_Messege.setObjectName(u"lb_Messege")
        self.lb_Messege.setStyleSheet(u"color: red;")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.lb_Messege)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 616, 33))
        self.menuAccount = QMenu(self.menubar)
        self.menuAccount.setObjectName(u"menuAccount")
        self.menuRegistered = QMenu(self.menuAccount)
        self.menuRegistered.setObjectName(u"menuRegistered")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.le_FirstName, self.le_LastName)
        QWidget.setTabOrder(self.le_LastName, self.cb_Status)
        QWidget.setTabOrder(self.cb_Status, self.le_Income)
        QWidget.setTabOrder(self.le_Income, self.pb_Submit)
        QWidget.setTabOrder(self.pb_Submit, self.pb_Exit)
        QWidget.setTabOrder(self.pb_Exit, self.pb_Login)

        self.menubar.addAction(self.menuAccount.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuAccount.addAction(self.actionNew_Account)
        self.menuAccount.addAction(self.menuRegistered.menuAction())
        self.menuAccount.addSeparator()
        self.menuAccount.addAction(self.actionAccount_Manager)
        self.menuRegistered.addAction(self.actionAccount_1)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionUpdate)

        self.retranslateUi(MainWindow)

        self.pb_Submit.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TaxiCal", None))
        self.actionNew_Account.setText(QCoreApplication.translate("MainWindow", u"New Account", None))
        self.actionAccount_1.setText(QCoreApplication.translate("MainWindow", u"Account 1", None))
        self.actionAccount_Manager.setText(QCoreApplication.translate("MainWindow", u"Account Manager", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionUpdate.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.gb_Name.setTitle(QCoreApplication.translate("MainWindow", u"Name", None))
        self.lb_FirstName.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.le_FirstName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"John", None))
        self.lb_LastName.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.le_LastName.setText("")
        self.le_LastName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Smith", None))
        self.gb_IncomeAndStatus.setTitle(QCoreApplication.translate("MainWindow", u"Income and Marital Status", None))
        self.lb_MaritalStatus.setText(QCoreApplication.translate("MainWindow", u"Marital Status", None))
        self.cb_Status.setItemText(0, QCoreApplication.translate("MainWindow", u"Select status", None))
        self.cb_Status.setItemText(1, QCoreApplication.translate("MainWindow", u"Single", None))
        self.cb_Status.setItemText(2, QCoreApplication.translate("MainWindow", u"Married (Joint Account)", None))
        self.cb_Status.setItemText(3, QCoreApplication.translate("MainWindow", u"Married (No Joint Account)", None))

        self.lb_Income.setText(QCoreApplication.translate("MainWindow", u"Income", None))
        self.le_Income.setPlaceholderText(QCoreApplication.translate("MainWindow", u"$0", None))
        self.groupBox.setTitle("")
        self.pb_Exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.pb_Submit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.lb_LoginQuestion.setText(QCoreApplication.translate("MainWindow", u"Already have account?", None))
        self.pb_Login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.lb_Messege.setText("")
        self.menuAccount.setTitle(QCoreApplication.translate("MainWindow", u"Account", None))
        self.menuRegistered.setTitle(QCoreApplication.translate("MainWindow", u"Registered", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

