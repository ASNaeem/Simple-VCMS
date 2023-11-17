from main import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

print("Test Merge")

print("merge?")
print("Test Merge 2.0")
class App(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        #self.ui = Ui_MainWindow()  # not needed if Ui_MainWindow was inherited (allows to get rid of the .ui from all lines)
        self.setupUi(self)
        # self.ui.button_submit.clicked.connect(self.authenticate)
        self.button_home.clicked.connect(self.show_home)
        self.button_appointments.clicked.connect(self.show_appointments)
        self.button_employees.clicked.connect(self.show_employees)
        self.button_inventory.clicked.connect(self.show_inventory)
        self.button_services.clicked.connect(self.show_services)
        self.button_patients.clicked.connect(self.show_patients)
        self.button_analytics.clicked.connect(self.show_analytics)
        self.button_billing.clicked.connect(self.show_billing)
        self.button_setting.clicked.connect(self.show_setting)
        self.button_support.clicked.connect(self.show_support)

    def show_home(self):
        self.stackedWidget.setCurrentIndex(0)

    def show_appointments(self):
        self.stackedWidget.setCurrentIndex(1)

    def show_employees(self):
        self.stackedWidget.setCurrentIndex(2)

    def show_inventory(self):
        self.stackedWidget.setCurrentIndex(3)

    def show_services(self):
        self.stackedWidget.setCurrentIndex(4)

    def show_patients(self):
        self.stackedWidget.setCurrentIndex(5)

    def show_analytics(self):
        self.stackedWidget.setCurrentIndex(6)

    def show_billing(self):
        self.stackedWidget.setCurrentIndex(7)

    def show_setting(self):
        self.stackedWidget.setCurrentIndex(8)

    def show_support(self):
        self.stackedWidget.setCurrentIndex(9)


"""
    def authenticate(self):
        # username = self.ui.userField.text()
        username = "user"
        password = "pass"
        if username == "user" and password == "pass":
            qtw.QMessageBox.information(self, "Success", "Login Success!")
        else:
            qtw.QMessageBox.critical(self, "Fail", "Login Failed!")
"""

if __name__ == "__main__":
    app = qtw.QApplication([])
    widget = App()
    widget.show()
    app.exec_()
