import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic, QtCore, QtGui
from qt_material import apply_stylesheet, list_themes
import warnings

warnings.filterwarnings('ignore')

 
class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon("resources/windowIcon.png"))
        uic.loadUi('MainUI.ui', self)
       
        self.page_appointment = uic.loadUi("AppointmentUI.ui")
        self.page_animal = uic.loadUi("AnimalUI.ui")
        self.page_inventory = uic.loadUi('InventoryUI.ui')
        self.page_setting = uic.loadUi('SettingUI.ui')
        self.page_support = uic.loadUi("SupportUI.ui")
        self.page_analytics_report = uic.loadUi("AnalyticsReportUI.ui")
        self.page_employee = uic.loadUi("EmployeeUI.ui")
        self.page_service = uic.loadUi("ServiceUI.ui")
       
        self.stackedWidget.addWidget(self.page_appointment)
        self.stackedWidget.addWidget(self.page_animal)
        self.stackedWidget.addWidget(self.page_inventory)
        self.stackedWidget.addWidget(self.page_setting)
        self.stackedWidget.addWidget(self.page_support)
        self.stackedWidget.addWidget(self.page_analytics_report)
        self.stackedWidget.addWidget(self.page_employee)
        self.stackedWidget.addWidget(self.page_service)
   
        self.button_appointments.clicked.connect(self.show_appointment)
        self.button_animal.clicked.connect(self.show_animal)
        self.button_inventory.clicked.connect(self.show_inventory)
        self.button_setting.clicked.connect(self.show_setting)
        self.button_support.clicked.connect(self.show_support)
        self.button_analytics.clicked.connect(self.show_analytics_report)
        self.button_employees.clicked.connect(self.show_employee)
        self.button_services.clicked.connect(self.show_service)
        
        self.page_setting.comboBox_themes.addItems(list_themes())
        self.page_setting.comboBox_themes.activated[str].connect(self.change_theme)
        with open("config.txt","w") as f:
            f.write(self.page_setting.comboBox_themes.currentText())
            
    def change_theme(self):
        apply_stylesheet(app, self.page_setting.comboBox_themes.currentText())
        
    def show_appointment(self):
        self.stackedWidget.setCurrentWidget(self.page_appointment)
        self.setWindowTitle("VCMS || Dashboard || Appointment")
    
    def show_animal(self):
        self.stackedWidget.setCurrentWidget(self.page_animal)
        self.setWindowTitle("VCMS || Dashboard || Animal")
        
    def show_inventory(self):
        self.stackedWidget.setCurrentWidget(self.page_inventory)
        self.setWindowTitle("VCMS || Dashboard || Inventory") 
           
    def show_setting(self):
        self.stackedWidget.setCurrentWidget(self.page_setting)
        self.setWindowTitle("VCMS || Dashboard || Setting")
    
    def show_support(self):
        self.stackedWidget.setCurrentWidget(self.page_support)
        self.setWindowTitle("VCMS || Dashboard || Support")

    def show_analytics_report(self):
        self.stackedWidget.setCurrentWidget(self.page_analytics_report)
        self.setWindowTitle("VCMS || Dashboard || AnalyticsReport")
    
    def show_employee(self):
        self.stackedWidget.setCurrentWidget(self.page_employee)
        self.setWindowTitle("VCMS || Dashboard || Employee")
    def show_service(self):
        self.stackedWidget.setCurrentWidget(self.page_service)
        self.setWindowTitle("VCMS || Dashboard || Service")


print(list_themes()[1])  
if __name__ == '__main__':
    
    app = QApplication([])
    """
    style_file = open("styles/aqua.qss", "r")
   
    with style_file:
        qss = style_file.read()
        app.setStyleSheet(qss)
    """
    window = MainApp()
    #window.show()
    #apply_stylesheet(app, theme='light_blue.xml')
    #apply_stylesheet(app, theme='light_blue.xml', css_file='custom.css')
    window.showMaximized()
    sys.exit(app.exec_())
