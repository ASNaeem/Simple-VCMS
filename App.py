import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MainUI.ui', self)
        
        self.page_appointment = uic.loadUi("AppointmentUI.ui")
        self.page_patient = uic.loadUi("PatientUI.ui")
        self.page_inventory = uic.loadUi('InventoryUI.ui')
        self.page_setting = uic.loadUi('SettingUI.ui')
        self.page_support = uic.loadUi("SupportUI.ui")
        
        self.stackedWidget.addWidget(self.page_appointment)
        self.stackedWidget.addWidget(self.page_patient)
        self.stackedWidget.addWidget(self.page_inventory)
        self.stackedWidget.addWidget(self.page_setting)
        self.stackedWidget.addWidget(self.page_support)
   
        self.button_patients.clicked.connect(self.show_appointment)
        self.button_patients.clicked.connect(self.show_patient)
        self.button_patients.clicked.connect(self.show_inventory)
        self.button_setting.clicked.connect(self.show_setting)
        self.button_support.clicked.connect(self.show_support)
        
    def show_inventory(self):
        self.stackedWidget.setCurrentWidget(self.page_inventory)
        self.setWindowTitle("VCMS||Dashboard||Inventory")
    
    def show_patient(self):
        self.stackedWidget.setCurrentWidget(self.page_patient)
        self.setWindowTitle("VCMS||Dashboard||Paitient")
        
    def show_inventory(self):
        self.stackedWidget.setCurrentWidget(self.page_inventory)
        self.setWindowTitle("VCMS||Dashboard||Inventory") 
           
    def show_setting(self):
        self.stackedWidget.setCurrentWidget(self.page_setting)
        self.setWindowTitle("VCMS||Dashboard||Setting")
    
    def show_support(self):
        self.stackedWidget.setCurrentWidget(self.page_support)
        self.setWindowTitle("VCMS||Dashboard||Support")
           
if __name__ == '__main__':
    app = QApplication([])
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
