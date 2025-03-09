
from json import JSONDecodeError
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon, QCloseEvent, QAction, QKeySequence, QShortcut, QDesktopServices
from PySide6.QtCore import QTimer, QUrl
import json
from decimal import Decimal
from UI.MainWindow import Ui_MainWindow
from UI.Login import Ui_Login
from UI.Inform import Ui_Inform
from UI.Database import Ui_NewRegistry
from UI.DatabaseDialogue import Ui_DatabaseQuestion
from UI.AccountManager import Ui_AccountManager
from UI.ConfirmDeletion import Ui_ConfirmDeletion
from UI.ChangePasscode import Ui_ChangePasscode
from UI.About import Ui_About
import sys, random, string
import pyperclip
from enum import Enum, auto
import os
sys.stdout = open(os.devnull, "w")
sys.path.append("E:\\Python")
from Classes import *


app_version = "5.0"


class AccountCase(Enum):
    New = auto()
    Registered = auto()
    def __str__(self):
        return self.name

class InputWindow(QtWidgets.QMainWindow ,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.account_case = AccountCase.New
        self.login = None
        self.inform = None
        self.database_question = None
        self.database_registry = None
        self.account_manager = None
        self.current_id = None
        self.about = None
        self.account_actions = {}
        self.logged_in_accounts_ids = []
        self.setupUi(self)
        self.actionAccount_Manager.setEnabled(False)
        self.actionAbout.triggered.connect(self.show_about)
        if loaded_variables:
            self.client = Person(variables=variables)
        else:
            self.client = Person()
        self.actionNew_Account.triggered.connect(self.switch_new)
        self.actionAccount_Manager.triggered.connect(self.pop_account_manager)
        self.le_FirstName.textEdited.connect(lambda: (self.check_first_name(), self.check(), self.capitalize()))
        self.le_LastName.textEdited.connect(lambda: (self.check_last_name(), self.check(), self.capitalize()))
        self.le_Income.textEdited.connect(lambda: (self.check_income(), self.check()))
        self.pb_Submit.clicked.connect(self.process)
        self.pb_Exit.clicked.connect(self.exit)
        self.pb_Login.clicked.connect(self.pop_login)
        self.cb_Status.currentTextChanged.connect(self.check)
        self.enter = QShortcut(QKeySequence("Return"), self)
        self.enter.activated.connect(self.pb_Submit.clicked)
    def show_about(self):
        self.about = About()
    def closeEvent(self, event:QCloseEvent):
        save_data_base_and_credentials()
        event.accept()
    def exit(self):
        save_data_base_and_credentials()
        self.close()
    def check(self):
        self.check_status()
        self.check_submit()
    def check_submit(self):
        if self.account_case == AccountCase.New:
            if self.check_input():
                self.pb_Submit.setEnabled(True)
            else:
                self.pb_Submit.setEnabled(False)
        elif self.account_case == AccountCase.Registered:
            if self.altered():
                self.pb_Submit.setEnabled(True)
            else:
                self.pb_Submit.setEnabled(False)
    def check_input2(self):
        first = False
        last = False
        income = False
        status = False
        if self.le_FirstName.text().isalpha() or self.le_FirstName.text() == "":
            first=True
        if self.le_LastName.text().isalpha() or self.le_LastName.text() == "":
            last=True
        if self.le_Income.text().replace("$", "").replace("¢", "").replace(".", "").isdigit() or self.le_Income.text() == "":
            income=True
        if self.cb_Status.currentText() != "Select status":
            status=True
        if first and last and income and status:
            return True
        else:
            return False
    def altered(self):
        cb_status_to_status = {
            "Single": "Single",
            "Married (Joint Account)": "MarriedJoint",
            "Married (No Joint Account)": "MarriedNoJoint"
        }
        if self.check_input2(): # note: input will never be equal to income str, since it's not allowed to input non digit, so instead translate input ot Money and compare it to self.client.income
            if self.le_FirstName.text() not in [self.client.first ,""] or self.le_LastName.text() not in [self.client.last, ""] or str_to_money_usd(self.le_Income.text()) not in [self.client.income, None] or cb_status_to_status[self.cb_Status.currentText()] != self.client.status.__str__():
                return True
            else:
                return False
    def critically_altered(self):
        cb_status_to_status = {
            "Single": "Single",
            "Married (Joint Account)": "MarriedJoint",
            "Married (No Joint Account)": "MarriedNoJoint"
        }
        if str_to_money_usd(self.le_Income.text()) not in [self.client.income, None] or cb_status_to_status[self.cb_Status.currentText()] != self.client.status.__str__():
            return True
    def check_status(self):
        if self.account_case == AccountCase.New:
            if self.le_FirstName.text().isalpha() and self.le_LastName.text().isalpha():
                self.cb_Status.setEnabled(True)
            else:
                self.cb_Status.setEnabled(False)
        elif self.account_case == AccountCase.Registered:
            if (self.le_FirstName.text().isalpha() or self.le_FirstName.text() == "") and (self.le_LastName.text().isalpha() or self.le_LastName.text() == ""):
                self.cb_Status.setEnabled(True)
            else:
                self.cb_Status.setEnabled(False)
    def pop_inform(self):
        self.inform = InformWindow()
    def pop_login(self):
        self.login = LoginWindow()
    def pop_account_manager(self):
        self.account_manager = AccountManager()
    def capitalize(self):
        self.le_FirstName.setText(self.le_FirstName.text().capitalize())
        self.le_LastName.setText(self.le_LastName.text().capitalize())
    def check_first_name(self):
        warning = "Name must be letters only!"
        if not self.le_FirstName.text().isalpha() and self.le_FirstName.text() != "":
            self.lb_Messege.setText(warning)
        else:
            if self.lb_Messege.text() == warning:
                self.lb_Messege.setText("")
    def check_income(self):
        warning = "Income must be digits only!"
        warning2 = "Income can't be zero"
        warning3 = "Points can't be more than one"
        if not self.le_Income.text().replace(".", "", 1).replace("$","").replace("¢", "").isdigit() and self.le_Income.text() != "":
            self.lb_Messege.setText(warning)
        elif self.le_Income.text() == "0":
            self.lb_Messege.setText(warning2)
        elif self.le_Income.text().count(".") > 1:
            self.lb_Messege.setText(warning3)
        else:
            if self.lb_Messege.text() in [warning, warning2]:
                self.lb_Messege.setText("")
    def check_last_name(self):
        warning = "Name must be letters only!"
        if not self.le_LastName.text().isalpha() and self.le_LastName.text() != "":
            self.lb_Messege.setText(warning)
        else:
            if self.lb_Messege.text() == warning:
                self.lb_Messege.setText("")
    def check_input(self):
       if self.le_FirstName.text().isalpha() and self.le_LastName.text().isalpha() and self.le_Income.text().replace("$","").replace(".", "", 1).replace("¢", "").isdigit() and self.cb_Status.currentText() != "Select status":
           return True
       else:
           return False
    def take_input(self):
        self.client.first = self.le_FirstName.text()
        self.client.last = self.le_LastName.text()
        self.client.income = Money(Decimal(str(self.le_Income.text().replace("$", "").replace("¢", ""))) * Decimal(100))
        if self.cb_Status.currentText() == "Single":
            self.client.status = MaritalStatus.Single
        elif self.cb_Status.currentText() == "Married (No Joint Account)":
            self.client.status = MaritalStatus.MarriedNoJoint
        elif self.cb_Status.currentText() == "Married (Joint Account)":
            self.client.status = MaritalStatus.MarriedJoint
    def process(self):
        if self.account_case == AccountCase.New:
            if self.check_input():
                self.lb_Messege.setStyleSheet("color:green;font:bold 14pt;")
                self.lb_Messege.setText("Calculating ...")
                self.disable_inputs()
                QTimer.singleShot(3000, lambda : (self.lb_Messege.setText(""), self.enable_inputs(), self.lb_Messege.setStyleSheet("color:red;font:bold 14pt;")))
                self.take_input()
                self.pop_inform()
                self.pb_Submit.setEnabled(False)
        elif self.account_case == AccountCase.Registered:
            if self.altered():
                self.disable_inputs()
                if self.critically_altered():
                    self.pop_inform()
                update_les = [self.le_FirstName, self.le_LastName, self.le_Income]
                for update_le in update_les:
                    if update_le.text() == "":
                        update_le.setText(update_le.placeholderText())
                self.take_input()
                database[self.current_id]=self.client.dictionary_format()
                self.pb_Submit.setIcon(QIcon(":Buttons/Generate.png"))
                self.pb_Submit.setText("Updating")
                QTimer.singleShot(2500,lambda : (self.pb_Submit.setIcon(QIcon(":Buttons/Copied.png")), self.pb_Submit.setText("Updated")))
                QTimer.singleShot(5000, lambda: (self.pb_Submit.setIcon(QIcon(":Buttons/submit.png")), self.pb_Submit.setText("Update"), self.pb_Submit.setEnabled(True), self.enable_inputs()))
                self.clear_le()
                self.set_ghost_values()
    def disable_inputs(self):
        self.le_FirstName.setEnabled(False)
        self.le_LastName.setEnabled(False)
        self.le_Income.setEnabled(False)
        self.cb_Status.setEnabled(False)
    def enable_inputs(self):
        self.le_FirstName.setEnabled(True)
        self.le_LastName.setEnabled(True)
        self.le_Income.setEnabled(True)
        self.cb_Status.setEnabled(True)
    def clear_le(self):
        self.le_FirstName.clear()
        self.le_LastName.clear()
        self.le_Income.clear()
    def clear_ghost(self):
        self.le_FirstName.setPlaceholderText("")
        self.le_LastName.setPlaceholderText("")
        self.le_Income.setPlaceholderText("")
    def set_default_ghost(self):
        self.le_FirstName.setPlaceholderText("John")
        self.le_LastName.setPlaceholderText("Smith")
        self.le_Income.setPlaceholderText("$0")
    def switch_registered(self):
        self.actionNew_Account.setChecked(False)
        self.actionAccount_Manager.setEnabled(True)
        self.account_case = AccountCase.Registered
        self.actionNew_Account.setChecked(False)
        self.pb_Submit.setText("Update")
        self.clear_le()
        self.set_ghost_values()
    def set_ghost_values(self):
        self.le_FirstName.setPlaceholderText(self.client.first)
        self.le_LastName.setPlaceholderText(self.client.last)
        self.le_Income.setPlaceholderText(self.client.income.__str__())
        self.cb_Status.setEnabled(True)
        if self.client.status == MaritalStatus.Single:
            self.cb_Status.setCurrentIndex(1)
        elif self.client.status == MaritalStatus.MarriedJoint:
            self.cb_Status.setCurrentIndex(2)
        elif self.client.status == MaritalStatus.MarriedNoJoint:
            self.cb_Status.setCurrentIndex(3)
    def switch_new(self):
        self.clear_le()
        self.set_default_ghost()
        self.account_case = AccountCase.New
        self.cb_Status.setCurrentIndex(0)
        self.actionNew_Account.setChecked(True)
        self.pb_Submit.setText("Submit")

    def update_logged_in_accounts(self):
        account_number = 0
        self.account_actions = {}
        self.menuRegistered.clear()
        if self.logged_in_accounts_ids:
            self.actionAccount_Manager.setEnabled(True)
            for a_id in self.logged_in_accounts_ids:
                account_number+=1
                self.account_actions[f"Account{account_number}"] = {}
                self.account_actions[f"Account{account_number}"]["Action"] = QAction(get_account_name(a_id,"fl"), self)
                self.account_actions[f"Account{account_number}"]["ID"] = a_id
                self.menuRegistered.addAction(self.account_actions[f"Account{account_number}"]["Action"])
                self.account_actions[f"Account{account_number}"]["Action"].triggered.connect(lambda _,iden=a_id :self.switch_to_account(iden))
        else:
            self.actionAccount_Manager.setEnabled(False)
    def switch_to_account(self, identity):
        self.current_id = identity
        self.only_checked()
        self.clear_le()
        self.client = dictionary_to_person(database, identity)
        self.set_ghost_values()
    def only_checked(self):
        for action_number, data in self.account_actions.items():
            if self.account_actions[action_number]["ID"] == self.current_id:
                self.account_actions[action_number]["Action"].setChecked(True)
                self.account_actions[action_number]["Action"].setCheckable(True)
            else:
                self.account_actions[action_number]["Action"].setChecked(False)
                self.account_actions[action_number]["Action"].setCheckable(True)
    def delete(self):
        delete_from_database(window.current_id)
        if self.current_id in self.logged_in_accounts_ids:
            self.logged_in_accounts_ids = [a_id for a_id in self.logged_in_accounts_ids if a_id != self.current_id]
            self.current_id = None
        self.update_logged_in_accounts()
        if self.account_actions:
            self.switch_to_account(self.logged_in_accounts_ids[0])
        else:
            self.switch_new()


class About(QtWidgets.QWidget, Ui_About):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.lb_VersionNumber.setText(app_version)
        self.tb_MyYouTube.clicked.connect(lambda :QDesktopServices.openUrl(QUrl("https://www.youtube.com/@The_Nubian_Gamer")))
        self.tb_MyGmail.clicked.connect(lambda :QDesktopServices.openUrl(QUrl("mailto:abdllaelsoni135@gmail.com?subject=TaxiCal")))
        self.tb_Mosh_YouTube.clicked.connect(lambda :QDesktopServices.openUrl(QUrl("https://www.youtube.com/c/programmingwithmosh")))
        self.tb_MoshWebsite.clicked.connect(lambda :QDesktopServices.openUrl(QUrl("https://codewithmosh.com/")))
        self.tb_JasonYouTube.clicked.connect(lambda :QDesktopServices.openUrl(QUrl("https://www.youtube.com/@josys363")))
        self.tb_ChatGPT.clicked.connect(lambda :QDesktopServices.openUrl(QUrl("https://openai.com/chatgpt")))
        self.tb_Freepik.clicked.connect(lambda :QDesktopServices.openUrl(QUrl("https://www.freepik.com/")))
    def closeEvent(self, event):
        window.activateWindow()
        event.accept()






class AccountManager(QtWidgets.QWidget, Ui_AccountManager):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.confirm_deletion = None
        self.gb_AccountName.setTitle(get_account_name(window.current_id,"fl"))
        self.tb_DeleteAccount.clicked.connect(self.attempt_delete_account)
        self.tb_ChangeID.clicked.connect(self.change_id)
        self.tb_Change_Passcode.clicked.connect(self.change_passcode)
        self.passcode = None
        self.show()
    def closeEvent(self, event, /):
        window.activateWindow()
        event.accept()
    def attempt_delete_account(self):
        self.confirm_deletion = ConfirmDeletion()
    def delete(self):
        window.delete()
        window.activateWindow()
        self.close()
    def change_id(self):
        pass
    def change_passcode(self):
        self.passcode = ChangePasscode()


class ChangePasscode(QtWidgets.QWidget, Ui_ChangePasscode):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.le_OldPasscode.textEdited.connect(self.check_to_allow_press)
        self.le_NewPasscode.textEdited.connect(self.check_to_allow_press)
        self.pb_Change.clicked.connect(self.change)
        self.pb_Cancel.clicked.connect(self.cancel)
    def cancel(self):
        self.close()
    def closeEvent(self, event):
        window.account_manager.activateWindow()
        event.accept()
    def change(self):
        if self.right_passcode:
            if self.valid_new_one:
                credentials[window.current_id] = self.le_NewPasscode.text()
                self.lb_Messege.setStyleSheet("color: green;")
                self.lb_Messege.setText("Passcode Changed.")
                QTimer.singleShot(1500, lambda :(self.close(), self.lb_Messege.setStyleSheet("color: red;")))
            else:
                self.lb_Messege.setText("Passcode must be 8 characters.")
        else:
            self.lb_Messege.setText("Incorrect Passcode!")
    def check_to_allow_press(self):
        if self.valid_guess and self.valid_new_one:
             self.pb_Change.setEnabled(True)
        else:
            self.pb_Change.setEnabled(False)
    @property
    def valid_guess(self):
        if len(self.le_OldPasscode.text()) == passcode_size:
            return True
    @property
    def right_passcode(self):
        if self.le_OldPasscode.text() == credentials[window.current_id]:
            return True
    @property
    def valid_new_one(self):
        if len(self.le_NewPasscode.text()) == passcode_size:
            return True

class ConfirmDeletion(QtWidgets.QWidget, Ui_ConfirmDeletion):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pb_Confirm.clicked.connect(self.confirm)
        self.pb_Cancel.clicked.connect(self.cancel)
        self.le_Passcode.textEdited.connect(self.check_to_allow_confirm)
        self.closing_method = "X"
    @property
    def valid_form_passcode(self):
        if len(self.le_Passcode.text()) == passcode_size:
            return True
    def check_to_allow_confirm(self):
        if self.valid_form_passcode:
            self.pb_Confirm.setEnabled(True)
        else:
            self.pb_Confirm.setEnabled(False)
    def confirm(self):
        if self.check_passcode():
            self.lb_Messege.setStyleSheet("color:green;font:bold 14pt;")
            self.lb_Messege.setText("Account deleted.")
            self.pb_Cancel.setEnabled(False)
            self.pb_Confirm.setEnabled(False)
            self.closing_method = "Ok"
            QTimer.singleShot(1500, lambda :self.close())
            window.account_manager.delete()
            window.activateWindow()
        else:
            self.lb_Messege.setStyleSheet("color:red; font: bold 14pt;")
            self.lb_Messege.setText("Wrong Passcode")
    def cancel(self):
        window.account_manager.activateWindow()
        self.closing_method = "Cancel"
        self.close()
    def check_passcode(self):
        if self.le_Passcode.text() == credentials[window.current_id]:
            return True
        else:
            return False
    def closeEvent(self, event):
        if self.closing_method == "X":
            event.ignore()
        else:
            event.accept()



class LoginWindow(Ui_Login, QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.le_Client_ID.textEdited.connect(self.check_login_button)
        self.le_Passcode.textEdited.connect(self.check_login_button)
        self.pb_Login.clicked.connect(self.attempt_login)
    @property
    def valid_form_id(self):
        if len(self.le_Client_ID.text()) == 16 and self.le_Client_ID.text().replace("-","").isdigit():
            return True
        else:
            return False
    @property
    def valid_form_passcode(self):
        if len(self.le_Passcode.text()) == passcode_size:
            return True
        else:
            return False
    def check_login_button(self):
        if self.valid_form_id and self.valid_form_passcode:
            self.pb_Login.setEnabled(True)
        else:
            self.pb_Login.setEnabled(False)
    def attempt_login(self):
        if self.le_Client_ID.text() not in window.logged_in_accounts_ids:
            if self.check_credentials():
                self.load_client()
                window.logged_in_accounts_ids.append(self.le_Client_ID.text())
                window.current_id = self.le_Client_ID.text()
                window.switch_registered()
                window.update_logged_in_accounts()
                window.inform = InformWindow()
                window.pb_Submit.setEnabled(False)
                self.close()
            elif self.check_credentials() is False:
                self.lb_Messege.setText("Incorrect Password!")
            else:
                self.lb_Messege.setText("Entry not found.")
        else:
            self.lb_Messege.setText("Already Logged in.")
    def load_client(self):
        window.client = dictionary_to_person(database,self.le_Client_ID.text())
    def check_credentials(self):
        if str(self.le_Client_ID.text()) in credentials:
            if str(self.le_Passcode.text()) == credentials[self.le_Client_ID.text()]:
                return True
            else: return False
        else:
            return None




class InformWindow(QtWidgets.QWidget, Ui_Inform):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_OK.clicked.connect(self.clicked_ok)
        self.te_Inform.setText(f'''
Income            : {window.client.income}
Deductions        : {window.client.deductions}
Taxable Income    : {window.client.taxable}
Federal Taxes     : {window.client.total_tax}
    ├─ Federal Income Tax  : {window.client.federal_income}
    ├─ Social Security Tax : {window.client.social_security}
    └─ Medicare Tax        : {window.client.medicare}

Net Income        : {window.client.post_tax}
Effective Rate    : {round((window.client.total_tax.value/window.client.income.value*Decimal("100")),2)}%
''')
        self.show()
        self.pb_Copy.clicked.connect(lambda: (self.copy(), self.copied()))
        self.closing_method = "X"
    def copy(self):
        pyperclip.copy(self.te_Inform.toPlainText())
    def clicked_ok(self):
        if window.account_case == AccountCase.New:
            window.database_question = DatabaseQuestion()
            self.closing_method = "Ok"
            self.close()
        elif window.account_case == AccountCase.Registered:
            self.close()
    def copied(self):
        self.pb_Copy.setIcon(QIcon(":Buttons/Copied.png"))
        QTimer.singleShot(3500, lambda: self.pb_Copy.setIcon(QIcon(":Buttons/Copy.png")))
    def closeEvent(self, event):
        if self.closing_method == "X":
            window.activateWindow()
        elif self.closing_method == "Ok":
            window.database_question.activateWindow()


class DatabaseQuestion(QtWidgets.QWidget, Ui_DatabaseQuestion):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.closing_method = "X"
        self.pb_OK.clicked.connect(self.attempt_addition_to_database)
        self.pb_Cancel.clicked.connect(self.close)
    def attempt_addition_to_database(self):
        window.database_registry = DatabaseNewRegistry()
        self.closing_method = "Ok"
        self.close()
    def closeEvent(self, event):
        if self.closing_method == "X":
            window.activateWindow()
        event.accept()
class DatabaseNewRegistry(QtWidgets.QWidget, Ui_NewRegistry):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.closing_method = "X"
        self.generated_ID=create_id()
        self.le_ID.setText(str(self.generated_ID))
        self.passcode = None
        self.pb_Generate.clicked.connect(self.generate_passcode)
        self.pb_Register.clicked.connect(self.register)
        self.pb_Copy.clicked.connect(lambda: (self.copy(), self.copied()))
        self.le_Passcode.textChanged.connect(self.check_to_allow_register)
        self.show()
    def check_to_allow_register(self):
        if self.valid_passcode:
            self.pb_Register.setEnabled(True)
        else:
            self.pb_Register.setEnabled(False)
    @property
    def valid_passcode(self):
        if len(self.le_Passcode.text()) == passcode_size:
            return True
    @property
    def formatted_credentials(self):
        return f'''ID: {self.le_ID.text()}
Passcode: {self.le_Passcode.text()}'''
    def copy(self):
        pyperclip.copy(self.formatted_credentials)
    def copied(self):
        self.pb_Copy.setIcon(QIcon(":Buttons/Copied.png"))
        QTimer.singleShot(3500, lambda: self.pb_Copy.setIcon(QIcon(":Buttons/Copy.png")))
    def add_to_database(self):
        add_to_database(window.client,self.generated_ID,self.le_Passcode.text())
    def register(self):
        self.add_to_database()
        window.switch_registered()
        window.logged_in_accounts_ids.append(self.le_ID.text())
        window.update_logged_in_accounts()
        window.switch_to_account(self.le_ID.text()) # note: current id is Non
        window.pb_Submit.setEnabled(False) # disable submit button
        self.closing_method = "Ok"
        self.close()
    def closeEvent(self, event):
        if self.closing_method == "X":
            # do something
            event.ignore()
        elif self.closing_method == "Ok":
            window.activateWindow()
            event.accept()
    def generate_passcode(self):
        self.pb_Generate.setIcon(QIcon(":Buttons/Generated.png"))
        QTimer.singleShot(400, lambda: self.pb_Generate.setIcon(QIcon(":Buttons/Generate.png")))
        self.passcode = create_passcode()
        self.le_Passcode.setText(str(self.passcode))
passcode_size = 8
database = {}
credentials = {}
variables = {}
loaded_variables = False
def load_variables():
    if os.path.exists("FederalVariables.json"):
        global variables, loaded_variables
        with open("FederalVariables.json", "r") as file:
            loaded_dictionary = json.load(file)
            if verify_dictionary_integrity(loaded_dictionary):
                variables = dictionary_to_variables(loaded_dictionary)
                loaded_variables = True
    else:
        pass

def create_id():
    while True:
        rand = random.randint((10 ** 15), (10 ** 16 - 1))
        if rand not in database:
            return rand
def create_passcode():
    pool = string.ascii_letters + string.digits
    return "".join(random.choices(pool, k=passcode_size))
def add_to_database(person, identity_code, passcode):
    database[str(identity_code)]=person.dictionary_format()
    credentials[str(identity_code)]=passcode
def delete_from_database(identity_code):
    if identity_code in database:
        del database[identity_code]
    if identity_code in credentials:
        del credentials[identity_code]
def load_database_and_credentials():
    global database
    global credentials
    try:
        with open("database.json", "r") as file:
            database = json.load(file)
    except (FileNotFoundError, JSONDecodeError):
        database = {}
    try:
        with open("credentials.json", "r") as file:
            credentials = json.load(file)
    except (FileNotFoundError, JSONDecodeError):
        credentials = {}
def save_data_base_and_credentials():
    global database
    global credentials
    with open("database.json", "w") as file:
        # noinspection PyTypeChecker
        json.dump(database, file)
    with open("credentials.json", "w") as file:
        # noinspection PyTypeChecker
        json.dump(credentials, file)


# noinspection PyUnboundLocalVariable
def get_account_name(identity, fl):
    account_found = False
    for a_id, details in database.items():
        if a_id == identity:
            account_found = True
            for key, value in details.items():
                if key == "first name":
                    first_name = value
                elif key == "last name":
                    last_name = value

    if account_found:
        if fl == "f":
            return first_name
        elif fl == "l":
            return last_name
        elif fl == "fl":
            return first_name + " " + last_name
    else:
        return None

load_database_and_credentials()
load_variables()
app = QtWidgets.QApplication(sys.argv)
window = InputWindow()
window.show()
sys.exit(app.exec())
