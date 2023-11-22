import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MainUI.ui', self)
        self.page_setting = uic.loadUi('SettingUI.ui')
        self.page_patient = uic.loadUi("PatientUI.ui")
        self.stackedWidget.addWidget(self.page_patient)
        self.stackedWidget.addWidget(self.page_setting)   
        self.button_patients.clicked.connect(self.show_patient)
        self.button_setting.clicked.connect(self.show_setting)

    def show_patient(self):
        self.stackedWidget.setCurrentWidget(self.page_patient)
        self.setWindowTitle("VCMS||Dashboard||Paitient")
        
    def show_setting(self):
        self.stackedWidget.setCurrentWidget(self.page_setting)
        self.setWindowTitle("VCMS||Dashboard||Setting")
       
if __name__ == '__main__':
    app = QApplication([])
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
