import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic, QtCore, QtGui
from qt_material import apply_stylesheet, list_themes
import warnings
import os 
os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'

warnings.filterwarnings("ignore")
theme_list = ["dark_blue.xml", "dark_medical.xml", "light_teal_500.xml"]


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon("resources/windowIcon.png"))
        uic.loadUi("MainUI.ui", self)

        self.page_appointment = uic.loadUi("AppointmentUI.ui")
        self.page_appointment_create = uic.loadUi("ApppointmentCreateUI.ui")
        self.page_appointment_modify = uic.loadUi("AppointmentModifyUI.ui")

        # self.page_animal = uic.loadUi("AnimalUI.ui")
        self.page_animal_info = uic.loadUi("AnimalInformationUI.ui")
        self.page_animal_reg = uic.loadUi("AnimalRegistrationUI.ui")
        self.page_animal_details = uic.loadUi("AnimalDetailsUI.ui")

        self.page_inventory = uic.loadUi("InventoryUI.ui")
        self.page_setting = uic.loadUi("SettingUI.ui")
        self.page_support = uic.loadUi("SupportUI.ui")
        self.page_analytics_report = uic.loadUi("AnalyticsReportUI.ui")
        self.page_employee = uic.loadUi("EmployeeUI.ui")
        self.page_service = uic.loadUi("ServiceUI.ui")
        self.page_daycare = uic.loadUi("DayCareUI.ui")
        self.page_billing = uic.loadUi("BillingUI.ui")
        self.page_expenses = uic.loadUi("ExpensesUI.ui")

        self.stackedWidget.addWidget(self.page_appointment)
        self.stackedWidget.addWidget(self.page_appointment_create)
        self.stackedWidget.addWidget(self.page_appointment_modify)

        # self.stackedWidget.addWidget(self.page_animal)
        self.stackedWidget.addWidget(self.page_animal_info)
        self.stackedWidget.addWidget(self.page_animal_reg)
        self.stackedWidget.addWidget(self.page_animal_details)

        self.stackedWidget.addWidget(self.page_inventory)
        self.stackedWidget.addWidget(self.page_daycare)
        self.stackedWidget.addWidget(self.page_billing)
        self.stackedWidget.addWidget(self.page_analytics_report)
        self.stackedWidget.addWidget(self.page_expenses)
        self.stackedWidget.addWidget(self.page_employee)
        self.stackedWidget.addWidget(self.page_service)
        self.stackedWidget.addWidget(self.page_setting)
        self.stackedWidget.addWidget(self.page_support)
        
        
        self.button_appointments.clicked.connect(self.show_appointment)
        self.page_appointment.button_app_create.clicked.connect(self.show_appointment_create)
        self.page_appointment.button_app_details.clicked.connect(self.show_appointment_modify)
        self.page_appointment_modify.button_app_back.clicked.connect(self.show_appointment)
        self.page_appointment_create.button_back_cancel.clicked.connect(self.show_appointment)
        self.page_appointment_create.button_create.clicked.connect(
            self.show_appointment
        )

        # self.button_animal.clicked.connect(self.show_animal)
        self.button_animal.clicked.connect(self.show_animal_info)
        self.page_animal_info.button_animal_reg.clicked.connect(self.show_animal_reg)
        self.page_animal_reg.button_reg_back.clicked.connect(self.show_animal_info)
        self.page_animal_info.button_animal_details.clicked.connect(
            self.show_animal_details
        )
        self.page_animal_details.button_animal_back.clicked.connect(
            self.show_animal_info
        )
        self.page_animal_reg.button_reg.clicked.connect(
            self.show_animal_info
        )

        self.button_daycare.clicked.connect(self.show_daycare)
        self.button_inventory.clicked.connect(self.show_inventory)
        self.button_analytics.clicked.connect(self.show_analytics_report)
        self.button_expenses.clicked.connect(self.show_expenses)
        self.button_employees.clicked.connect(self.show_employee)
        self.button_services.clicked.connect(self.show_service)
        self.button_setting.clicked.connect(self.show_setting)
        self.button_support.clicked.connect(self.show_support)
        self.button_billing.clicked.connect(self.show_billing)
        # self.page_animal.button_animal_register_new.clicked.connect(self.show_animal_reg)
        # self.page_animal.button_reg_back.clicked.connect(self.show_animal_)
        self.page_setting.comboBox_themes.addItems(list_themes())
        self.page_setting.comboBox_themes.activated[str].connect(self.change_theme)
        self.change_theme()

    def show_daycare(self):
        self.stackedWidget.setCurrentWidget(self.page_daycare)

    def show_appointment(self):
        self.stackedWidget.setCurrentWidget(self.page_appointment)
        self.setWindowTitle("VCMS || Dashboard || Appointment")

    def show_appointment_modify(self):
        self.stackedWidget.setCurrentWidget(self.page_appointment_modify)
        self.setWindowTitle("VCMS || Dashboard || Appointment Details")

    def show_appointment_create(self):
        self.stackedWidget.setCurrentWidget(self.page_appointment_create)
        self.setWindowTitle("VCMS || Dashboard || Create New Appointment")

    def show_animal_info(self):
        self.stackedWidget.setCurrentWidget(self.page_animal_info)
        self.setWindowTitle("VCMS || Dashboard || Animals")

    def show_animal_reg(self):
        self.stackedWidget.setCurrentWidget(self.page_animal_reg)
        # self.setWindowTitle("VCMS || Dashboard || Animals")

    def show_animal_details(self):
        self.stackedWidget.setCurrentWidget(self.page_animal_details)
        # self.setWindowTitle("VCMS || Dashboard || Animal")

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

    def show_billing(self):
        self.stackedWidget.setCurrentWidget(self.page_billing)
        self.setWindowTitle("VCMS || Dashboard || Billing")

    def show_expenses(self):
        self.stackedWidget.setCurrentWidget(self.page_expenses)
        self.setWindowTitle("VCMS || Dashboard || Expenses")
        
    def change_theme(self):
        apply_stylesheet(
            app,
            self.page_setting.comboBox_themes.currentText(),
            invert_secondary=False,
            extra=extra,
        )
        with open("config.txt", "w") as f:
            f.write(self.page_setting.comboBox_themes.currentText())


extra = {
    # Density Scale
    "density_scale": "-1",
}
if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    # window.show()
    with open("config.txt", "r") as f:
        read = f.read()
        apply_stylesheet(app, theme=read, extra=extra)
        window.page_setting.comboBox_themes.setCurrentText(read)
    # apply_stylesheet(app, theme='light_blue.xml', css_file='custom.css')
    window.adjustSize()
    window.showMaximized()
    # window.showFullScreen()
    sys.exit(app.exec_())
