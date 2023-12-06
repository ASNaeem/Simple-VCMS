import sys
import warnings
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtCore import QDate, Qt
from qt_material import apply_stylesheet, list_themes
from datetime import date
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox
from MySQLHandler import MySQLHandler

from Employee import Employees, fetch_employees, add_employee, delete_employee
from Service import Services, fetch_services
from Animal import Animals, fetch_animals, delete_record_from_db
from Billing import Billings, fetch_billings
from Item import Items, fetch_items
from DayCareService import Day_Care_Service, fetch_day_care
from Expense import Expenses, fetch_expenses


os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

warnings.filterwarnings("ignore")
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
        self.set_employee_table()
        self.set_day_care_table()
        self.set_expense_table()

        ### functionalities ######
        self.page_animal_details.button_add_record.clicked.connect(self.add_record)
        self.page_animal_details.button_record_delete.clicked.connect(self.delete_record)
        self.page_animal_reg.button_reg.clicked.connect(self.create_new_animal)

        self.page_employee.button_edit.clicked.connect(self.populate_employee)
        self.page_employee.button_edit_information_6.clicked.connect(self.update_employee)
        self.page_employee.button_register_employee_6.clicked.connect(self.register_employee)
        self.page_employee.button_delete_information_6.clicked.connect(self.delete_employee)
        ##################### End Init #####################

    def add_record(self):
        page = self.page_animal_details
        table = page.table_animal_record
        diagnosis = page.line_new_record.text().strip()
        if diagnosis:
            selected_item = self.page_animal_info.table_animal.selectedItems()
            animal_id = int(selected_item[0].text())
            animal_object = None
            for animal in Animals:
                if animal.animal_id == animal_id:
                    animal_object = animal
                    break

            animal.add_record(diagnosis)
            self.set_records_table(animal)
            # self.add_records_to_table(-1, animal.medical_records[-1])

            page.line_new_record.clear()

        else:
            print("Input a diagnosis record to add!")

    ##################### Page switching #####################
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
        self.page_animal_info.table_animal.clearSelection()
        self.setWindowTitle("VCMS || Dashboard || Animals")

    def show_animal_reg(self):
        self.stackedWidget.setCurrentWidget(self.page_animal_reg)
        # self.setWindowTitle("VCMS || Dashboard || Animals")

    def show_animal_details(self):
        selected_item = self.page_animal_info.table_animal.selectedItems()
        if selected_item:
            animal_id = int(selected_item[0].text())
            animal = None
            for ob in Animals:
                if ob.animal_id == animal_id:
                    animal = ob
                    break
            self.stackedWidget.setCurrentWidget(self.page_animal_details)
            page = self.page_animal_details

            page.line_animal_id.setText(str(animal.animal_id))
            page.line_animal_name.setText(animal.animal_name)

            # date_object = datetime.strptime(str(animal.birth_date), "%Y-%m-%d").date()
            qdate = QDate(
                animal.birth_date.year, animal.birth_date.month, animal.birth_date.day
            )
            page.date_animal_birth.setDate(qdate)

            # date = QDate.fromString(str(animal.birth_date), date_format)
            qdate = QDate(
                animal.reg_date.year, animal.reg_date.month, animal.reg_date.day
            )
            page.date_animal_reg.setDate(qdate)

            page.line_animal_species.setText(animal.species)
            page.line_animal_breed.setText(animal.breed)
            page.line_animal_color.setText(animal.color)

            # date = QDate.fromString(str(animal.birth_date), date_format)
            # page.date_animal_birth.setDate(date)

            page.line_animal_warning.setText(animal.behavioral_warning)
            page.line_animal_condition.setText(animal.med_condition)
            page.line_owner_name.setText(animal.owner_name)
            page.line_owner_phone.setText(animal.phone)
            page.line_owner_email.setText(animal.email)
            page.line_owner_address.setText(animal.address)

            if animal.gender.lower() == "male":
                page.rbutton_gender_male.setChecked(True)
            else:
                page.rbutton_gender_female.setChecked(True)

            if animal.sterilized.lower() == "yes":
                page.rbutton_ster_yes.setChecked(True)
            else:
                page.rbutton_ster_no.setChecked(True)

            # setting records table #
            self.set_records_table(animal)

            # self.setWindowTitle("VCMS || Dashboard || Animal")
        else:
            print("Select a row to view more details")

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

        employee_info = [
            f"{employee.name}({employee.employee_id})" for employee in Employees
        ]
        combo_box = self.page_expenses.comboBox
        print(employee_info)
        combo_box.addItems(employee_info)
        combo_box.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)

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

    ##################### Animal ########################

    def create_new_animal(self):
        page = self.page_animal_reg
        animal_name = page.line_reg_name.text()
        reg_date = page.date_reg.text()
        species = page.line_reg_species.text()
        breed = page.line_reg_breed.text()
        color = page.line_reg_color.text()

        if page.rbutton_reg_male.isChecked():
            gender = "Male"
        elif page.rbutton_reg_female.isChecked():
            gender = "Female"

        if page.rbutton_reg_ster_yes.isChecked():
            sterilized = "Yes"
        elif page.rbutton_reg_ster_no.isChecked():
            sterilized = "No"

        med_condition = page.line_reg_condition.text()
        owner_name = page.line_reg_oname.text()
        phone = page.line_reg_phone.text()
        email = page.line_reg_email.text()
        address = page.line_reg_address.text()
        birth_date = page.date_reg_birth.text()
        behavioral_warning = page.line_reg_warning.text()
        # Convert birth_date to "YYYY-MM-DD" format
        reg_date_obj = datetime.strptime(str(reg_date), "%Y-%m-%d").date()
        birth_date_obj = datetime.strptime(str(birth_date), "%Y-%m-%d").date()

        if not all(
            [
                animal_name,
                reg_date,
                species,
                breed,
                color,
                gender,
                sterilized,
                med_condition,
                owner_name,
                phone,
                email,
                address,
                birth_date,
                behavioral_warning,
            ]
        ):
            QMessageBox.warning(self, "Warning", "Please fill in all fields.")
            return
        try:
            mysql_handler = MySQLHandler()
            mysql_handler.connect()
            query = "insert into animals (animal_name, birth_date, sterilized, gender, species, breed, color, behavioral_warning, owner_name, email, phone, address, reg_date, med_condition) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            values = (
                animal_name,
                birth_date_obj,
                sterilized,
                gender,
                species,
                breed,
                color,
                behavioral_warning,
                owner_name,
                email,
                phone,
                address,
                reg_date_obj,
                med_condition,
            )
            mysql_handler.execute_query(query, values)
            print("Entry Success!")
            mysql_handler.disconnect()

            self.set_animal_table()

            page.line_reg_name.clear()
            page.date_reg.clear()
            page.line_reg_species.clear()
            page.line_reg_breed.clear()
            page.line_reg_color.clear()

            # Radio button clear kaj kore na :)
            # Data table e double kore show kore :)

            page.rbutton_reg_male.setChecked(False)
            page.rbutton_reg_female.setChecked(False)
            page.rbutton_reg_ster_yes.setChecked(False)
            page.rbutton_reg_ster_no.setChecked(False)

            page.line_reg_condition.clear()
            page.line_reg_oname.clear()
            page.line_reg_phone.clear()
            page.line_reg_email.clear()
            page.line_reg_address.clear()
            page.date_reg_birth.clear()
            page.line_reg_warning.clear()
        except Exception as err:
            print("Entry Failed!", err)

    def delete_record(self):
        selected_animal_row = self.page_animal_info.table_animal.currentRow()
        animal_id = int(
            self.page_animal_info.table_animal.item(selected_animal_row, 0).text()
        )

        page = self.page_animal_details
        table = page.table_animal_record
        selected_row = table.currentRow()
        if selected_row != -1:
            row_data = [
                table.item(selected_row, col).text()
                for col in range(table.columnCount())
            ]
            print(row_data)
            table.removeRow(selected_row)
            delete_record_from_db(animal_id, row_data)
        else:
            print("Select an item to delete!")

    def set_records_table(self, animal):
        self.page_animal_details.table_animal_record.clearContents()
        self.page_animal_details.table_animal_record.setRowCount(0)
        for row, record in enumerate(animal.medical_records):
            self.add_records_to_table(row, record)

    def set_animal_table(self):
        fetch_animals()
        for row, animal in enumerate(Animals):
            self.add_animal_to_table(row, animal)

    def add_animal_to_table(self, row, animal):
        header = self.page_animal_info.table_animal.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.page_animal_info.table_animal.insertRow(row)
        self.page_animal_info.table_animal.setItem(
            row, 0, QTableWidgetItem(str(animal.animal_id))
        )
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.page_animal_info.table_animal.setItem(
            row, 1, QTableWidgetItem(animal.animal_name)
        )
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        # self.page_animal_info.table_animal.setItem(row, 2, QTableWidgetItem(str(animal.birth_date)))
        # self.page_animal_info.table_animal.setItem(row, 3, QTableWidgetItem(str(animal.sterilized)))
        # self.page_animal_info.table_animal.setItem(row, 4, QTableWidgetItem(animal.gender))
        self.page_animal_info.table_animal.setItem(
            row, 2, QTableWidgetItem(animal.species)
        )
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.page_animal_info.table_animal.setItem(
            row, 3, QTableWidgetItem(animal.breed)
        )
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.page_animal_info.table_animal.setItem(
            row, 4, QTableWidgetItem(animal.color)
        )
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        # self.page_animal_info.table_animal.setItem(row, 8, QTableWidgetItem(animal.behavioral_warning))
        self.page_animal_info.table_animal.setItem(
            row, 5, QTableWidgetItem(animal.owner_name)
        )
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        # self.page_animal_info.table_animal.setItem(row, 10, QTableWidgetItem(animal.email))
        self.page_animal_info.table_animal.setItem(
            row, 6, QTableWidgetItem(animal.phone)
        )
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        # self.page_animal_info.table_animal.setItem(row, 12, QTableWidgetItem(animal.address))
        # self.page_animal_info.table_animal.setItem(row, 13, QTableWidgetItem(str(animal.reg_date)))
        # self.page_animal_info.table_animal.setItem(row, 14, QTableWidgetItem(animal.med_condition))

    def add_records_to_table(self, row, record):
        table = self.page_animal_details.table_animal_record
        header = table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        table.insertRow(row)
        table.setItem(row, 0, QTableWidgetItem(str(record[1])))
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 1, QTableWidgetItem(str(record[0])))
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

    ################# Employee ###################

    def clear_employee_fields():
        page.line_name_6.clear()
        page.line_email_6.clear()
        page.line_personal_contact_6.clear()
        page.line_home_6.clear()
        page.line_address_6.clear()
        page.line_salary_6.clear()

    def populate_employee(self):
        selected_item = self.page_employee.table_employee.selectedItems()
        if selected_item:
            employee_id = int(selected_item[0].text())
            employee = None
            for emp in Employees:
                if emp.employee_id == employee_id:
                    employee = emp
                    break

            page = self.page_employee

            page.line_name_6.setText(employee.name)
            page.line_email_6.setText(employee.email)
            page.line_personal_contact_6.setText(employee.phone[0])
            page.line_home_6.setText(employee.phone[1])
            page.line_address_6.setText(employee.address)
            page.line_salary_6.setText(str(employee.salary))

            jdate = QDate(
                employee.joining_date.year,
                employee.joining_date.month,
                employee.joining_date.day,
            )
            page.dateEdit_joining_date_6.setDate(jdate)

            if employee.employee_status.lower() == "working":
                page.rb_working.setChecked(True)
            else:
                page.rb_on_leave.setChecked(True)

            page.combobox_access_level_6.setCurrentText(str(employee.access_level))
            page.comboBox_designation_6.setCurrentText(employee.designation)

    def update_employee(self):
        ...

    def register_employee(self):
        page = self.page_employee

        name = page.line_name_6.text()
        email = page.line_email_6.text()
        phone = page.line_personal_contact_6.text()
        alt_phone = page.line_home_6.text()
        address = page.line_address_6.text()
        salary = page.line_salary_6.text()

        jdate = QDate(
            employee.joining_date.year,
            employee.joining_date.month,
            employee.joining_date.day,
        )

        joining_date = page.dateEdit_joining_date_6.setDate(jdate)

        if page.rb_working.isChecked():
            status = "Working"
        elif page.rb_on_leave.isChecked():
            status = "On Leave"

        access_level = ""
        designation = ""

        ##combo box baki parina T-T Chatgpt ko bhi pucha, kuch samajh me nahi aya :3

        if not all([name, email, phone, alt_phone, address, salary, status]):
            ...

    def delete_employee(self):
        ...

    def set_employee_table(self):
        fetch_employees()
        for row, employee in enumerate(Employees):
            self.add_employee_to_table(row, employee)

    def add_employee_to_table(self, row, employee):
        header = self.page_employee.table_employee.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        table = self.page_employee.table_employee
        table.insertRow(row)
        table.setItem(row, 0, QTableWidgetItem(str(employee.employee_id)))
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 1, QTableWidgetItem(str(employee.name)))
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 2, QTableWidgetItem(str(employee.email)))
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 3, QTableWidgetItem(str(employee.phone[0])))
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 4, QTableWidgetItem(str(employee.phone[1])))
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 5, QTableWidgetItem(str(employee.address)))
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 6, QTableWidgetItem(str(employee.designation)))
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 7, QTableWidgetItem(str(employee.access_level)))
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 8, QTableWidgetItem(str(employee.working_hours)))
        header.setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 9, QTableWidgetItem(str(employee.salary)))
        header.setSectionResizeMode(9, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 10, QTableWidgetItem(str(employee.joining_date)))
        header.setSectionResizeMode(10, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 11, QTableWidgetItem(str(employee.employee_status)))
        header.setSectionResizeMode(11, QtWidgets.QHeaderView.ResizeToContents)

    ################### End of Employee ###################

    ################### Day Care Service ##################
    def set_day_care_table(self):
        fetch_day_care()
        for row, day_care in enumerate(Day_Care_Service):
            self.add_day_care_to_table(row, day_care)

    def add_day_care_to_table(self, row, day_care):
        header = self.page_daycare.table_care.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        table = self.page_daycare.table_care
        table.insertRow(row)
        table.setItem(row, 0, QTableWidgetItem(str(day_care.day_Care_id)))
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 1, QTableWidgetItem(str(day_care.animal_id)))
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 2, QTableWidgetItem(str(day_care.day_care_date)))
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 3, QTableWidgetItem(str(day_care.start_time)))
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 4, QTableWidgetItem(str(day_care.end_time)))
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 5, QTableWidgetItem(str(day_care.notes)))
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)

    ################### Day Care Service End ##################

    ################### Expenses ##################
    def set_expense_table(self):
        fetch_expenses()
        for row, expense in enumerate(Expenses):
            self.add_expense_to_table(row, expense)

    def add_expense_to_table(self, row, expense):
        header = self.page_expenses.table_expense.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        table = self.page_expenses.table_expense
        table.insertRow(row)
        table.setItem(row, 0, QTableWidgetItem(str(expense.expense_id)))
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 1, QTableWidgetItem(str(expense.issuer_id)))
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 2, QTableWidgetItem(str(expense.expense_date)))
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 3, QTableWidgetItem(str(expense.amount)))
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 4, QTableWidgetItem(str(expense.justification)))
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)

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
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        table = self.page_billing.table_bill
        table.insertRow(row)
        table.setItem(row, 0, QTableWidgetItem(str(billing.billing_id)))
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 1, QTableWidgetItem(str(billing.day_care_id)))
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 2, QTableWidgetItem(str(billing.appointment_id)))
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 3, QTableWidgetItem(str(billing.payment_date)))
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 4, QTableWidgetItem(str(billing.total_amount)))
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 5, QTableWidgetItem(str(billing.adjustment)))
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        table.setItem(row, 6, QTableWidgetItem(str(billing.status)))
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)

    def add_billing_service_to_service_table(self, rowService, service):
        header = self.page_billing.table_show_service.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        table = self.page_billing.table_show_service

        table.setItem(rowService, 0, QTableWidgetItem(service.service_id))
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)

        table.setItem(rowService, 1, QTableWidgetItem(service.name))
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        table.setItem(rowService, 2, QTableWidgetItem(service.cost))
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

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
