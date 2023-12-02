import sys
from employee import Employees, fetch_employees, add_employee, delete_employee
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import QtWidgets, uic, QtCore, QtGui
from qt_material import apply_stylesheet, list_themes
import warnings
import os

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
from Operations import Animals, fetch_animals, Billings, fetch_billings, Services

# warnings.filterwarnings("ignore")
theme_list = ["dark_blue.xml", "dark_medical.xml", "light_teal_500.xml"]


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon("resources/windowIcon.png"))
        uic.loadUi("MainUI.ui", self)

        self.page_appointment = uic.loadUi("AppointmentUI.ui")
        self.page_appointment_create = uic.loadUi("AppointmentCreateUI.ui")
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
        self.page_appointment.button_app_create.clicked.connect(
            self.show_appointment_create
        )
        self.page_appointment.button_app_details.clicked.connect(
            self.show_appointment_modify
        )
        self.page_appointment_modify.button_apt_back.clicked.connect(
            self.show_appointment
        )
        self.page_appointment_create.button_back_cancel.clicked.connect(
            self.show_appointment
        )
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
        self.page_animal_reg.button_reg.clicked.connect(self.show_animal_info)

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
        # self.change_theme()
        self.set_animal_table()
        self.set_bill_table()

        ##################### End Init #####################


    ##################### Page switching#####################
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

    #####   Setting    #####
    def change_theme(self):
        apply_stylesheet(
            app,
            self.page_setting.comboBox_themes.currentText(),
            invert_secondary=False,
            extra=extra,
        )
        with open("config.txt", "w") as f:
            f.write(self.page_setting.comboBox_themes.currentText())

    ## Animal ##
    def set_animal_table(self):
        fetch_animals()
        for row, animal in enumerate(Animals):
            self.add_animal_to_table(row, animal)

    def add_animal_to_table(self, row, animal):
        header = self.page_animal_info.table_animal.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.page_animal_info.table_animal.insertRow(row)
        self.page_animal_info.table_animal.setItem(
            row, 0, QTableWidgetItem(str(animal.animal_id))
        )
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.page_animal_info.table_animal.setItem(
            row, 1, QTableWidgetItem(animal.animal_name)
        )
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        # self.page_animal_info.table_animal.setItem(row, 2, QTableWidgetItem(str(animal.birth_date)))
        # self.page_animal_info.table_animal.setItem(row, 3, QTableWidgetItem(str(animal.sterilized)))
        # self.page_animal_info.table_animal.setItem(row, 4, QTableWidgetItem(animal.gender))
        self.page_animal_info.table_animal.setItem(
            row, 2, QTableWidgetItem(animal.species)
        )
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.page_animal_info.table_animal.setItem(
            row, 3, QTableWidgetItem(animal.breed)
        )
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.page_animal_info.table_animal.setItem(
            row, 4, QTableWidgetItem(animal.color)
        )
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        # self.page_animal_info.table_animal.setItem(row, 8, QTableWidgetItem(animal.behavioral_warning))
        self.page_animal_info.table_animal.setItem(
            row, 5, QTableWidgetItem(animal.owner_name)
        )
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        # self.page_animal_info.table_animal.setItem(row, 10, QTableWidgetItem(animal.email))
        self.page_animal_info.table_animal.setItem(
            row, 6, QTableWidgetItem(animal.phone)
        )
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        # self.page_animal_info.table_animal.setItem(row, 12, QTableWidgetItem(animal.address))
        # self.page_animal_info.table_animal.setItem(row, 13, QTableWidgetItem(str(animal.reg_date)))
        # self.page_animal_info.table_animal.setItem(row, 14, QTableWidgetItem(animal.med_condition))

    ################# Employee ###################

    def set_employee_table(self):
        fetch_employees()
        for row, employee in enumerate(Employees):
            self.add_employee_to_table(row, employee)

    def add_employee_to_table(self, row, employee):
        header = self.page_employee.table_employee.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        table = self.page_employee.table_employee
        table.insertRow(row)
        table.setItem(row, 0, QTableWidgetItem(str(employee.employee_id)))
        table.setItem(row, 1, QTableWidgetItem(str(employee.name)))
        table.setItem(row, 2, QTableWidgetItem(str(employee.email)))
        table.setItem(row, 3, QTableWidgetItem(str(employee.phone[0])))
        table.setItem(row, 3, QTableWidgetItem(str(employee.phone[1])))
        table.setItem(row, 4, QTableWidgetItem(str(employee.address)))
        table.setItem(row, 5, QTableWidgetItem(str(employee.designation)))
        table.setItem(row, 6, QTableWidgetItem(str(employee.access_level)))
        table.setItem(row, 7, QTableWidgetItem(str(employee.working_hours)))
        table.setItem(row, 8, QTableWidgetItem(str(employee.salary)))
        table.setItem(row, 9, QTableWidgetItem(str(employee.joining_date)))
        ############## Need fixing #######################

    ################# End of Employee ###################

    ################### Billing ##################

    def set_bill_table(self):
        fetch_billings()
        for row, billing in enumerate(Billings):
            self.add_billing_to_table(row, billing)

            service_details = self.get_service_details(billing.services, Services)
            for rowService, service in enumerate(service_details):
                self.add_billing_service_to_service_table(rowService, service)

    def get_service_details(self, service_ids, services):
        return [service for service in services if service.service_id in service_ids]

    def add_billing_to_table(self, row, billing):
        header = self.page_billing.table_bill.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        table = self.page_billing.table_bill
        table.insertRow(row)
        table.setItem(row, 0, QTableWidgetItem(str(billing.billing_id)))
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        table.setItem(row, 1, QTableWidgetItem(str(billing.day_care_id)))
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        table.setItem(row, 2, QTableWidgetItem(str(billing.appointment_id)))
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        table.setItem(row, 3, QTableWidgetItem(str(billing.payment_date)))
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        table.setItem(row, 4, QTableWidgetItem(str(billing.total_amount)))
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        table.setItem(row, 5, QTableWidgetItem(str(billing.adjustment)))
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        table.setItem(row, 6, QTableWidgetItem(str(billing.status)))
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)

    def add_billing_service_to_service_table(self, rowService, service):
        header = self.page_billing.table_show_service.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        table = self.page_billing.table_show_service

        table.setItem(rowService, 0, QTableWidgetItem(service.service_id))
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        table.setItem(rowService, 1, QTableWidgetItem(service.name))
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        table.setItem(rowService, 2, QTableWidgetItem(service.cost))
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

################### End Billing ##################                

    ################### Appointment ##################
    def make_appointment(self):
        apt = self.page_appointment_create
        date = apt.date_apt.selectedDate()
        time = apt.time_apt.selectedTime()
        # appointment_service = self.page_appointment_create.cb_service.currentText()
        reason = apt.line_reason.currentText()
        first_name = apt.line_oname.currentText()
        last_name = apt.line_lname.currentText()
        phone = apt.line_phone.currentText()
        email = apt.line_email.currentText()
        address = apt.line_address.currentText()
        # animal_id = apt.line_aid.currentText()
        animal_name = apt.line_aname.currentText()
        specicies = apt.line_species.currentText()
        breed = apt.line_breed.currentText()
        color = apt.line_colors.currentText()
        behaviour = apt.line_behave.currentText()
        birth = apt.date_appt_birth.selectedDate()
        reg_date = apt.date_appt_reg.selectedDate()
        name = first_name + " " + last_name
        op.add_appointment(
            date,
            time,
            reason,
            name,
            phone,
            address,
            animal_name,
            species,
            breed,
            color,
            behaviour,
            birth,
            reg_date,
        )

        def populate_appointment(self):
            ...


####

#### UI density Scaling modifier ####
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
