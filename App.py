import sys
import warnings
import os
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidgetItem,
    QWidget,
    QCheckBox,
)

from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from qt_material import apply_stylesheet, list_themes
from datetime import date
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox
from MySQLHandler import MySQLHandler

from Employee import (
    Employees,
    fetch_employees,
    add_employee,
    delete_employee,
    update_employee_phone_to_db,
    update_employee_to_db,
)
from Appointment import (
    Appointments,
    fetch_appointment,
    add_appointment,
    delete_appointment,
)
from Service import (
    Services,
    add_service,
    delete_service,
    update_service,
    fetch_services,
)
from Animal import (
    Animals,
    fetch_animals,
    delete_record_from_db,
    delete_animal_from_db,
    update_animal_from_db,
)
from Billing import Billings, fetch_billings, delete_bill
from Item import Items, fetch_items
from DayCareService import (
    Day_Care_Service,
    fetch_day_care,
    delete_day_care,
    add_day_care,
    update_daycare_to_db,
)
from Expense import Expenses, fetch_expenses, delete_expenses, update_expense_to_db


os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

warnings.filterwarnings("ignore")
theme_list = ["dark_blue.xml", "dark_medical.xml", "light_teal_500.xml"]


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon("resources/windowIcon.png"))
        uic.loadUi("MainUI.ui", self)

        # self.page_animal = uic.loadUi("AnimalUI.ui")
        self.page_appointment = uic.loadUi("AppointmentUI.ui")
        self.page_appointment_create = uic.loadUi("AppointmentCreateUI.ui")
        self.page_appointment_modify = uic.loadUi("AppointmentModifyUI.ui")
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

        # self.stackedWidget.addWidget(self.page_animal)
        self.stackedWidget.addWidget(self.page_appointment)
        self.stackedWidget.addWidget(self.page_appointment_create)
        self.stackedWidget.addWidget(self.page_appointment_modify)
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

        # self.button_animal.clicked.connect(self.show_animal)
        self.button_animal.clicked.connect(self.show_animal_info)
        self.button_daycare.clicked.connect(self.show_daycare)
        self.button_inventory.clicked.connect(self.show_inventory)
        self.button_analytics.clicked.connect(self.show_analytics_report)
        self.button_expenses.clicked.connect(self.show_expenses)
        self.button_employees.clicked.connect(self.show_employee)
        self.button_services.clicked.connect(self.show_service)
        self.button_setting.clicked.connect(self.show_setting)
        self.button_support.clicked.connect(self.show_support)
        self.button_billing.clicked.connect(self.show_billing)
        self.button_appointments.clicked.connect(self.show_appointment)

        self.page_setting.comboBox_themes.addItems(list_themes())
        self.page_setting.comboBox_themes.activated[str].connect(self.change_theme)
        # self.change_theme()

        self.set_animal_table()
        self.set_bill_table()
        self.set_employee_table()
        self.set_day_care_table()
        self.set_expense_table()
        self.set_appointment_table()
        self.set_service_table()

        ##################### functionalities ###################################
        # self.page_animal.button_animal_register_new.clicked.connect(self.show_animal_reg)
        # self.page_animal.button_reg_back.clicked.connect(self.show_animal_)
        self.page_animal_info.button_animal_reg.clicked.connect(self.show_animal_reg)
        self.page_animal_reg.button_reg_back.clicked.connect(self.show_animal_info)
        self.page_animal_info.button_animal_details.clicked.connect(
            self.show_animal_details
        )
        self.page_animal_details.button_animal_back.clicked.connect(
            self.show_animal_info
        )
        self.page_animal_reg.button_reg.clicked.connect(self.show_animal_info)
        self.page_animal_details.button_add_record.clicked.connect(self.add_record)
        self.page_animal_details.button_record_delete.clicked.connect(
            self.delete_record
        )

        self.page_expenses.button_expense_edit.clicked.connect(self.populate_expense)
        self.page_expenses.button_expense_delete.clicked.connect(self.delete_expense)
        self.page_expenses.button_expense_add.clicked.connect(self.create_new_expense)
        self.page_expenses.button_expense_save.clicked.connect(self.update_expense)

        self.page_animal_reg.button_reg.clicked.connect(self.create_new_animal)
        self.page_animal_info.button_delete_animal_info.clicked.connect(
            self.delete_animal
        )
        self.page_animal_details.button_animal_save.clicked.connect(self.update_animal)

        self.page_employee.button_edit.clicked.connect(self.populate_employee)
        self.page_employee.button_save.clicked.connect(self.update_employee)
        self.page_employee.button_register.clicked.connect(self.register_employee)
        self.page_employee.button_delete.clicked.connect(self.delete_employee)

        # self.page_billing.button_bill_add.clicked.connect(self.add_new_bill)
        self.page_billing.button_bill_edit.clicked.connect(self.populate_bill)
        self.page_billing.button_bill_save.clicked.connect(self.update_bill)
        self.page_billing.button_bill_delete.clicked.connect(self.delete_bill)

        self.page_service.button_service_cancel.clicked.connect(self.populate_service)
        self.page_service.button_service_add.clicked.connect(self.add_new_service)
        self.page_service.button_service_save.clicked.connect(
            self.update_existing_service
        )
        self.page_service.button_service_delete.clicked.connect(
            self.delete_existing_service
        )

        self.page_appointment.button_app_create.clicked.connect(
            self.show_appointment_create
        )
        self.page_appointment.button_app_details.clicked.connect(
            self.show_appointment_modify  # populate selected row's information to modify page's fields
        )
        self.page_appointment.button_delete_appointment.clicked.connect(
            self.delete_existing_appointment
        )
        self.page_appointment_create.button_create.clicked.connect(
            self.create_appointment
        )
        self.page_appointment_create.button_back_cancel.clicked.connect(
            self.show_appointment
        )
        self.page_appointment_create.chk_box_new_animal.stateChanged.connect(
            self.checkbox_state_changed
        )
        self.page_appointment_modify.button_apt_back.clicked.connect(
            self.show_appointment
        )

        self.page_daycare.button_care_delete.clicked.connect(self.delete_from_daycare)
        self.page_daycare.button_care_edit.clicked.connect(self.populate_daycare)
        self.page_daycare.button_care_save.clicked.connect(self.update_daycare)

        self.page_animal_info.line_animal_search.textChanged.connect(self.search_animal)
        self.page_expenses.line_expense_search.textChanged.connect(self.search_expense)
        self.page_employee.line_search_6.textChanged.connect(self.search_employee)
        self.page_daycare.line_care_search.textChanged.connect(self.search_daycare)
        self.page_appointment.line_appointment_search.textChanged.connect(
            self.search_appointment
        )
        self.page_billing.line_bill_search.textChanged.connect(self.search_bill)
        self.page_service.line_service_search.textChanged.connect(self.search_service)
        self.page_inventory.line_inventory_search.textChanged.connect(self.search_Item)
        ##################### End Init #####################

    def search_Item(self, text):
        try:
            table = self.page_inventory.table_inventory
            for row in range(table.rowCount()):
                match = any(
                    text.lower() in table.item(row, col).text().lower()
                    for col in range(table.columnCount())
                )
                table.setRowHidden(row, not match)
        except Exception as err:
            print(f"Error Fetching(search_Item): {err}")

    def search_service(self, text):
        try:
            table = self.page_service.table_service
            for row in range(table.rowCount()):
                match = any(
                    text.lower() in table.item(row, col).text().lower()
                    for col in range(table.columnCount())
                )
                table.setRowHidden(row, not match)
        except Exception as err:
            print(f"Error Fetching(search_service): {err}")

    def search_animal(self, text):
        try:
            table = self.page_animal_info.table_animal
            for row in range(table.rowCount()):
                match = any(
                    text.lower() in table.item(row, col).text().lower()
                    for col in range(table.columnCount())
                )
                table.setRowHidden(row, not match)
        except Exception as err:
            print(f"Error Fetching(search_animal): {err}")

    def add_record(self):
        try:
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
        except Exception as err:
            print(f"Error Fetching(add_record): {err}")

    ##################### Page switching #####################
    def show_daycare(self):
        try:
            self.stackedWidget.setCurrentWidget(self.page_daycare)
            self.page_daycare.table_care.setCurrentCell(-1, 0)
            self.set_day_care_table()
        except Exception as err:
            print(f"Error Fetching(show_daycare): {err}")

    def show_appointment(self):
        try:
            self.stackedWidget.setCurrentWidget(self.page_appointment)
            self.page_appointment.appointment_table_widget_2.setCurrentCell(-1, 0)
            self.setWindowTitle("VCMS || Dashboard || Appointment")
        except Exception as err:
            print(f"Error Fetching(show_appointment): {err}")

    def show_appointment_modify(self):
        try:
            self.stackedWidget.setCurrentWidget(self.page_appointment_modify)
            selected_item = (
                self.page_appointment.appointment_table_widget_2.selectedItems()
            )
            if selected_item:
                appointment_id = int(selected_item[0].text())
                # animal_id = int(selected_item[1].text())
                appointment = None

                for ap in Appointments:
                    if ap.appointment_id == appointment_id:
                        appointment = ap
                        break

                page = self.page_appointment_modify

                page.line_apt_id.setText(str(appointment.appointment_id))
                page.line_apt_animal_id.setText(str(appointment.animal_id))
                page.line_apt_owner_address.setText(appointment.owner_name)
                page.line_apt_species.setText(appointment.species)
                page.line_apt_phone.setText(appointment.phone_number)
                page.line_apt_status.setText(appointment.appointment_status)
                page.text_visit_reason.setText(appointment.visit_reason)
                print(type(appointment.appointment_date))
                print(appointment.appointment_date)
                qdate = QDate(
                    appointment.appointment_date.year,
                    appointment.appointment_date.month,
                    appointment.appointment_date.day,
                )
                page.date_apt.setDate(qdate)

                """qtime = QTime(
                    appointment.appointment_time.hour,
                    appointment.appointment_time.minute,
                    appointment.appointment_time.second
                )"""

                qtime = QTime.fromString(str(appointment.appointment_time), "hh:mm:ss")

                page.time_apt.setTime(qtime)

            else:
                print("No row selected! Select a row to view more details.")

            self.setWindowTitle("VCMS || Dashboard || Appointment Details")

            vet_name = []
            for employee in Employees:
                if "vet" in employee.designation.lower():
                    vet_name.append((employee.name, employee.employee_id))
            vet_info = [f"{vet[0]} ({vet[1]})" for vet in vet_name]
            combo_box = self.page_appointment_modify.comboBox_vet_name
            combo_box.addItems(vet_info)
            combo_box.completer().setCompletionMode(
                QtWidgets.QCompleter.PopupCompletion
            )
        except Exception as err:
            print(f"Error Fetching(show_appointment_modify): {err}")

    def show_appointment_create(self):
        try:
            self.stackedWidget.setCurrentWidget(self.page_appointment_create)
            self.setWindowTitle("VCMS || Dashboard || Create New Appointment")
        except Exception as err:
            print(f"Error Fetching(show_appointment_create): {err}")

    def show_animal_info(self):
        try:
            self.stackedWidget.setCurrentWidget(self.page_animal_info)
            self.page_animal_info.table_animal.setCurrentCell(-1, 0)
            self.setWindowTitle("VCMS || Dashboard || Animals")
            self.set_animal_table()
        except Exception as err:
            print(f"Error Fetching(show_animal_info): {err}")

    def show_animal_reg(self):
        try:
            self.stackedWidget.setCurrentWidget(self.page_animal_reg)
            # self.setWindowTitle("VCMS || Dashboard || Animals")
        except Exception as err:
            print(f"Error Fetching(show_animal_reg): {err}")

    def show_animal_details(self):
        try:
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
                    animal.birth_date.year,
                    animal.birth_date.month,
                    animal.birth_date.day,
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
        except Exception as err:
            print(f"Error Fetching(show_animal_details): {err}")

    def show_inventory(self):
        try:
            self.stackedWidget.setCurrentWidget(self.page_inventory)
            self.page_inventory.table_inventory.setCurrentCell(-1, 0)
            self.setWindowTitle("VCMS || Dashboard || Inventory")
            # self.stackedWidget.setCurrentWidget(self.page_inventory)
            # self.setWindowTitle("VCMS || Dashboard || Inventory")
        except Exception as err:
            print(f"Error Fetching(show_inventory): {err}")

    def show_setting(self):
        try:
            self.stackedWidget.setCurrentWidget(self.page_setting)
            self.setWindowTitle("VCMS || Dashboard || Setting")
        except Exception as err:
            print(f"Error Fetching(show_setting): {err}")

    def show_support(self):
        try:
            self.stackedWidget.setCurrentWidget(self.page_support)
            self.setWindowTitle("VCMS || Dashboard || Support")
        except Exception as err:
            print(f"Error Fetching(show_support): {err}")

    def show_analytics_report(self):
        try:
            self.stackedWidget.setCurrentWidget(self.page_analytics_report)
            self.setWindowTitle("VCMS || Dashboard || AnalyticsReport")
            self.stackedWidget.setCurrentWidget(self.page_analytics_report)
            self.setWindowTitle("VCMS || Dashboard || AnalyticsReport")
        except Exception as err:
            print(f"Error Fetching(show_analytics_report): {err}")

    def show_employee(self):
        try:
            self.stackedWidget.setCurrentWidget(self.page_employee)
            self.page_employee.table_employee.setCurrentCell(-1, 0)
            # print(self.page_employee.table_employee.currentRow())
            self.setWindowTitle("VCMS || Dashboard || Employee")

        except Exception as err:
            print(f"Error Fetching(show_employee): {err}")

    def show_service(self):
        try:
            self.stackedWidget.setCurrentWidget(self.page_service)
            self.page_service.table_service.setCurrentCell(-1, 0)
            self.setWindowTitle("VCMS || Dashboard || Service")
            self.set_service_table()
        except Exception as err:
            print(f"Error Fetching(show_service): {err}")

    def show_billing(self):
        try:
            self.stackedWidget.setCurrentWidget(self.page_billing)
            self.page_billing.table_bill.setCurrentCell(-1, 0)
            self.setWindowTitle("VCMS || Dashboard || Billing")
        except Exception as err:
            print(f"Error Fetching(show_billing): {err}")

    def show_expenses(self):
        try:
            self.stackedWidget.setCurrentWidget(self.page_expenses)
            self.page_expenses.table_expense.setCurrentCell(-1, 0)
            self.setWindowTitle("VCMS || Dashboard || Expenses")
            employee_info = [
                f"{employee.name} ({employee.employee_id})" for employee in Employees
            ]
            employee_info.insert(0, "Select")
            combo_box = self.page_expenses.comboBox
            combo_box.addItems(employee_info)
            combo_box.completer().setCompletionMode(
                QtWidgets.QCompleter.PopupCompletion
            )
            self.set_expense_table()
        except Exception as err:
            print(f"Error Fetching(show_expenses): {err}")

    #####   Setting    #####
    def change_theme(self):
        try:
            apply_stylesheet(
                app,
                self.page_setting.comboBox_themes.currentText(),
                invert_secondary=False,
                extra=extra,
            )
            with open("config.txt", "w") as f:
                f.write(self.page_setting.comboBox_themes.currentText())
        except Exception as err:
            print(f"Error Fetching(change_theme): {err}")

    ##################### Animal ########################
    def clear_animal_fields(self):
        try:
            page = self.page_animal_reg
            page.line_reg_name.clear()
            page.date_reg.clear()
            page.line_reg_species.clear()
            page.line_reg_breed.clear()
            page.line_reg_color.clear()

            # Radio button clear kaj kore na :)
            page.button_group_gender.setExclusive(False)
            page.button_group_sterilized.setExclusive(False)
            page.rbutton_reg_male.setChecked(False)
            page.rbutton_reg_female.setChecked(False)
            page.rbutton_reg_ster_yes.setChecked(False)
            page.rbutton_reg_ster_no.setChecked(False)
            page.button_group_gender.setExclusive(True)
            page.button_group_sterilized.setExclusive(True)

            page.line_reg_condition.clear()
            page.line_reg_oname.clear()
            page.line_reg_phone.clear()
            page.line_reg_email.clear()
            page.line_reg_address.clear()
            page.date_reg_birth.clear()
            page.line_reg_warning.clear()
        except Exception as err:
            print(f"Error Fetching(clear_animal_fields): {err}")

    def create_new_animal(self):
        try:
            page = self.page_animal_reg
            current_widget = self.stackedWidget.setCurrentWidget(page)
            animal_name = page.line_reg_name.text()
            reg_date = page.date_reg.text()
            species = page.line_reg_species.text()
            breed = page.line_reg_breed.text()
            color = page.line_reg_color.text()

            gender = ""
            if page.rbutton_reg_male.isChecked():
                gender = "Male"
            elif page.rbutton_reg_female.isChecked():
                gender = "Female"

            sterilized = ""
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
                QMessageBox.warning(
                    current_widget, "Warning", "Please fill in all fields."
                )
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
                print("Animal Entry Success!")
                mysql_handler.disconnect()
                self.set_animal_table()
                self.clear_animal_fields()
                self.show_animal_info()
            except Exception as err:
                print("Animal Entry Failed!", err)

        except Exception as err:
            print(f"Error Fetching(create_new_animal): {err}")

    def update_animal(self):
        try:
            page = self.page_animal_details

            animal_id = int(page.line_animal_id.text())
            name = page.line_animal_name.text()

            # date_object = datetime.strptime(str(animal.birth_date), "%Y-%m-%d").date()
            bdate = page.date_animal_birth.date().toPyDate()

            # date = QDate.fromString(str(animal.birth_date), date_format)
            rdate = page.date_animal_reg.date().toPyDate()

            species = page.line_animal_species.text()
            breed = page.line_animal_breed.text()
            color = page.line_animal_color.text()

            warning = page.line_animal_warning.text()
            condition = page.line_animal_condition.text()
            oname = page.line_owner_name.text()
            phone = page.line_owner_phone.text()
            email = page.line_owner_email.text()
            address = page.line_owner_address.text()

            gender = page.button_group_gender.checkedButton().text()
            sterilized = page.button_group_sterilized.checkedButton().text()
            update_animal_from_db(
                name,
                bdate,
                sterilized,
                gender,
                species,
                breed,
                color,
                warning,
                oname,
                email,
                phone,
                address,
                rdate,
                condition,
                animal_id,
            )
            self.show_animal_info()
        except Exception as err:
            print(f"Animal update failed: {err}")

    def delete_animal(self):
        try:
            page = self.page_animal_info
            table = page.table_animal
            current_widget = self.stackedWidget.setCurrentWidget(page)
            selected_animal_row = table.currentRow()
            if selected_animal_row != -1:
                animal_id = int(table.item(selected_animal_row, 0).text())
                table.removeRow(selected_animal_row)
                delete_animal_from_db(animal_id)
            else:
                QMessageBox.warning(
                    current_widget, "Warning", "Select a record to delete!"
                )
        except Exception as err:
            print(f"Error Fetching(delete_animal): {err}")

    def delete_record(self):
        try:
            page = self.page_animal_details
            selected_animal_row = self.page_animal_info.table_animal.currentRow()
            current_widget = self.stackedWidget.setCurrentWidget(page)
            print(f"this is delete record 1: {selected_animal_row}")
            animal_id = int(
                self.page_animal_info.table_animal.item(selected_animal_row, 0).text()
            )
            page = self.page_animal_details
            table = page.table_animal_record
            selected_row = table.currentRow()
            if selected_row != -1:
                print(f"this is delete record 1: {selected_row}")
                row_data = [
                    table.item(selected_row, col).text()
                    for col in range(table.columnCount())
                ]
                # print(row_data)
                table.removeRow(selected_row)
                delete_record_from_db(animal_id, row_data)
            else:
                QMessageBox.warning(
                    current_widget, "Warning", "Select a record to delete!"
                )
        except Exception as err:
            print(f"Error Fetching(delete_record): {err}")

    def set_records_table(self, animal):
        try:
            self.page_animal_details.table_animal_record.clearContents()
            self.page_animal_details.table_animal_record.setRowCount(0)
            self.page_animal_details.table_animal_record.setSortingEnabled(False)
            for row, record in enumerate(animal.medical_records):
                self.add_records_to_table(row, record)
            self.page_animal_details.table_animal_record.setSortingEnabled(True)
        except Exception as err:
            print(f"Error Fetching(set_records_table): {err}")

    def set_animal_table(self):
        try:
            self.page_animal_info.table_animal.clearContents()
            self.page_animal_info.table_animal.setRowCount(0)
            fetch_animals()
            self.page_animal_info.table_animal.setSortingEnabled(False)
            for row, animal in enumerate(Animals):
                self.add_animal_to_table(row, animal)
            self.page_animal_info.table_animal.setSortingEnabled(True)
        except Exception as err:
            print(f"Error Fetching(set_animal_table): {err}")

    def add_animal_to_table(self, row, animal):
        try:
            header = self.page_animal_info.table_animal.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            table = self.page_animal_info.table_animal
            self.page_animal_info.table_animal.insertRow(row)
            self.page_animal_info.table_animal.setItem(
                row, 0, QTableWidgetItem(str(animal.animal_id))
            )
            # header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            self.page_animal_info.table_animal.setItem(
                row, 1, QTableWidgetItem(animal.animal_name)
            )
            # self.page_animal_info.table_animal.setItem(row, 2, QTableWidgetItem(str(animal.birth_date)))
            # self.page_animal_info.table_animal.setItem(row, 3, QTableWidgetItem(str(animal.sterilized)))
            # self.page_animal_info.table_animal.setItem(row, 4, QTableWidgetItem(animal.gender))
            self.page_animal_info.table_animal.setItem(
                row, 2, QTableWidgetItem(animal.species)
            )
            # header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            self.page_animal_info.table_animal.setItem(
                row, 3, QTableWidgetItem(animal.breed)
            )
            # header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            self.page_animal_info.table_animal.setItem(
                row, 4, QTableWidgetItem(animal.color)
            )
            # header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
            # self.page_animal_info.table_animal.setItem(row, 8, QTableWidgetItem(animal.behavioral_warning))
            self.page_animal_info.table_animal.setItem(
                row, 5, QTableWidgetItem(animal.owner_name)
            )
            # header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
            # self.page_animal_info.table_animal.setItem(row, 10, QTableWidgetItem(animal.email))
            self.page_animal_info.table_animal.setItem(
                row, 6, QTableWidgetItem(animal.phone)
            )
            # header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
            # self.page_animal_info.table_animal.setItem(row, 12, QTableWidgetItem(animal.address))
            # self.page_animal_info.table_animal.setItem(row, 13, QTableWidgetItem(str(animal.reg_date)))
            # self.page_animal_info.table_animal.setItem(row, 14, QTableWidgetItem(animal.med_condition))
            self.resize_columns_to_contents(table, header)
        except Exception as err:
            print(f"Error Fetching(add_animal_to_table): {err}")

    def add_records_to_table(self, row, record):
        try:
            table = self.page_animal_details.table_animal_record
            header = table.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            table.insertRow(row)
            table.setItem(row, 0, QTableWidgetItem(str(record[1])))
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            table.setItem(row, 1, QTableWidgetItem(str(record[0])))
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        except Exception as err:
            print(f"Error Fetching(add_records_to_table): {err}")

    #################### Animal End #####################

    ##################### Employee ######################

    def clear_employee_fields(self):
        try:
            self.page_employee.line_name_6.clear()
            self.page_employee.line_email_6.clear()
            self.page_employee.line_personal_contact_6.clear()
            self.page_employee.line_home_6.clear()
            self.page_employee.line_address_6.clear()
            self.page_employee.line_salary_6.clear()
            self.page_employee.dateEdit_joining_date_6.setDate(QDate(2000, 1, 1))
            self.page_employee.rb_working.setChecked(False)
            self.page_employee.rb_on_leave.setChecked(False)
            self.page_employee.comboBox_designation_6.setCurrentIndex(0)
            self.page_employee.combobox_access_level_6.setCurrentIndex(0)
        except Exception as err:
            print(f"Error Clearing Employee Fields: {err}")

    def search_employee(self, text):
        try:
            table = self.page_employee.table_employee
            for row in range(table.rowCount()):
                match = any(
                    text.lower() in table.item(row, col).text().lower()
                    for col in range(table.columnCount())
                )
                table.setRowHidden(row, not match)
        except Exception as err:
            print(f"Error Fetching(search_employee): {err}")

    def populate_employee(self):
        try:
            selected_item = self.page_employee.table_employee.selectedItems()
            if selected_item and self.page_employee.button_edit.text() == "Edit":
                self.page_employee.button_edit.setText("Cancel")
                self.page_employee.button_register.setEnabled(False)
                # selected_item = self.page_employee.table_employee.selectedItems()
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
                page.line_employee_password.setText(employee.password)

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
            else:
                self.page_employee.button_edit.setText("Edit")
                self.clear_employee_fields()
                self.page_employee.button_register.setEnabled(True)
                self.show_employee()
        except Exception as err:
            print(f"Error Fetching Employee: {err}")

    def update_employee(self):
        try:
            selected_item = self.page_employee.table_employee.selectedItems()
            if selected_item:
                employee_id = int(selected_item[0].text())
                phone_prev = selected_item[3].text()
                alt_phone_prev = selected_item[4].text()

                page = self.page_employee
                name = page.line_name_6.text()
                email = page.line_email_6.text()
                phone = page.line_personal_contact_6.text()
                alt_phone = page.line_home_6.text()
                address = page.line_address_6.text()
                salary = page.line_salary_6.text()
                password = page.line_employee_password.text()
                joining_date = page.dateEdit_joining_date_6.text()
                joining_date_obj = datetime.strptime(
                    str(joining_date), "%Y-%m-%d"
                ).date()
                if page.rb_working.isChecked():
                    employee_status = "Working"
                elif page.rb_on_leave.isChecked():
                    employee_status = "On Leave"
                if page.combobox_access_level_6.currentIndex != 0:
                    access_level = page.combobox_access_level_6.currentText()
                if page.comboBox_designation_6.currentIndex != 0:
                    designation = page.comboBox_designation_6.currentText()

                update_employee_to_db(
                    employee_id,
                    name,
                    email,
                    password,
                    address,
                    designation,
                    access_level,
                    salary,
                    joining_date,
                    employee_status,
                )
                update_employee_phone_to_db(
                    employee_id, phone, phone_prev, alt_phone, alt_phone_prev
                )

                self.set_employee_table()
            else:
                print("Select a Row!")
        except Exception as err:
            print(f"Error Fetching(update_employee): {err}")

    def register_employee(self):
        try:
            page = self.page_employee
            current_widget = self.stackedWidget.setCurrentWidget(page)
            name = page.line_name_6.text()
            email = page.line_email_6.text()
            phone = page.line_personal_contact_6.text()
            alt_phone = page.line_home_6.text()
            address = page.line_address_6.text()
            salary = page.line_salary_6.text()
            password = page.line_employee_password.text()
            joining_date = page.dateEdit_joining_date_6.text()
            joining_date_obj = datetime.strptime(str(joining_date), "%Y-%m-%d").date()
            if page.rb_working.isChecked():
                employee_status = "Working"
            elif page.rb_on_leave.isChecked():
                employee_status = "On Leave"
            if page.combobox_access_level_6.currentIndex != 0:
                access_level = page.combobox_access_level_6.currentText()
            if page.comboBox_designation_6.currentIndex != 0:
                designation = page.comboBox_designation_6.currentText()
            if not all(
                [
                    name,
                    email,
                    password,
                    phone,
                    alt_phone,
                    address,
                    salary,
                    joining_date_obj,
                    employee_status,
                    access_level,
                    designation,
                ]
            ):
                QMessageBox.warning(
                    current_widget, "Warning", "Please fill in all fields."
                )
                return
            mysql_handler = MySQLHandler()
            mysql_handler.connect()
            query_employee = "insert into employees (name, email, password, address, designation, access_level, salary, joining_date, employee_status) values (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
            data_employee = (
                name,
                email,
                password,
                address,
                designation,
                access_level,
                salary,
                joining_date_obj,
                employee_status,
            )
            mysql_handler.execute_query(query_employee, data_employee)
            query_fetch_id = "select employee_id, name from employees order by employee_id desc limit 1;"
            row = mysql_handler.fetch_data(query_fetch_id)
            employee_id = row[0][0]
            query_phone = "insert into phones (employee_id, phone) values (%s, %s);"
            data_phone1 = (employee_id, phone)
            data_phone2 = (employee_id, alt_phone)
            mysql_handler.execute_query(query_phone, data_phone1)
            mysql_handler.execute_query(query_phone, data_phone2)
            mysql_handler.disconnect()
            print("Entry Success!")
            self.clear_employee_fields()

            self.set_employee_table()
        except Exception as err:
            print(f"Employee Entry Failed: {err}")

    def delete_employee(self):
        try:
            page = self.page_employee
            current_widget = self.stackedWidget.setCurrentWidget(page)
            table = page.table_employee
            selected_employee_row = table.currentRow()
            if selected_employee_row != -1:
                employee_id = int(table.item(selected_employee_row, 0).text())
                table.removeRow(selected_employee_row)
                delete_employee(employee_id)
            else:
                QMessageBox.warning(
                    current_widget, "Warning", "Select a record to delete!"
                )
        except Exception as err:
            print(f"Error Fetching(delete_employee): {err}")

    def set_employee_table(self):
        try:
            self.page_employee.table_employee.clearContents()
            self.page_employee.table_employee.setRowCount(0)
            fetch_employees()
            self.page_employee.table_employee.setSortingEnabled(False)
            for row, employee in enumerate(Employees):
                self.add_employee_to_table(row, employee)
            self.page_employee.table_employee.setSortingEnabled(True)
        except Exception as err:
            print(f"Error Fetching(set_employee_table): {err}")

    def add_employee_to_table(self, row, employee):
        try:
            header = self.page_employee.table_employee.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            table = self.page_employee.table_employee
            table.insertRow(row)
            table.setItem(row, 0, QTableWidgetItem(str(employee.employee_id)))
            table.setItem(row, 1, QTableWidgetItem(str(employee.name)))
            table.setItem(row, 2, QTableWidgetItem(str(employee.email)))
            table.setItem(row, 3, QTableWidgetItem(str(employee.phone[0])))
            table.setItem(row, 4, QTableWidgetItem(str(employee.phone[1])))
            table.setItem(row, 5, QTableWidgetItem(str(employee.address)))
            table.setItem(row, 6, QTableWidgetItem(str(employee.designation)))
            table.setItem(row, 7, QTableWidgetItem(str(employee.access_level)))
            table.setItem(row, 8, QTableWidgetItem(str(employee.salary)))
            table.setItem(row, 9, QTableWidgetItem(str(employee.joining_date)))
            table.setItem(row, 10, QTableWidgetItem(str(employee.employee_status)))
            self.resize_columns_to_contents_alternate(table)
            table.resizeColumnToContents(0)
            table.resizeColumnToContents(6)
            table.resizeColumnToContents(7)
            table.resizeColumnToContents(8)
            table.resizeColumnToContents(9)
            table.resizeColumnToContents(10)
            # self.resize_columns_to_contents_alternate2(table)
        except Exception as err:
            print(f"Error Fetching(add_employee_to_table): {err}")

    ################### End of Employee ###################

    ################### Day Care Service ##################
    """def add_to_daycare(self):
        try:
            ...
        except Exception as err:
            print(f"Error Fetching (add_to_daycare): {err}")"""

    def clear_daycare_fields(self):
        try:
            page = self.page_daycare
            page.line_care_id.clear()
            page.line_animal_id.clear()
            page.date_care.setDate(QDate(2000, 1, 1))
            page.time_care_start.setTime(QTime(00, 00, 00))
            page.time_care_end.setTime(QTime(00, 00, 00))
            page.text_care_notes.clear()

        except Exception as err:
            print(f"Clear DayCare Fields Failed!: {err}")

    def search_daycare(self, text):
        try:
            table = self.page_daycare.table_care
            for row in range(table.rowCount()):
                match = any(
                    text.lower()
                    in (table.item(row, col).text() if table.item(row, col) else "")
                    for col in range(table.columnCount())
                )
                table.setRowHidden(row, not match)
        except Exception as err:
            print(f"Error Fetching(search_daycare): {err}")

    def delete_from_daycare(self):
        try:
            page = self.page_daycare
            current_widget = self.stackedWidget.setCurrentWidget(page)
            table = page.table_care
            selected_daycare_row = table.currentRow()
            if selected_daycare_row != -1:
                daycare_id = int(table.item(selected_daycare_row, 0).text())
                table.removeRow(selected_daycare_row)
                delete_day_care(daycare_id)
            else:
                QMessageBox.warning(
                    current_widget, "Warning", "Select a record to delete!"
                )
        except Exception as err:
            print(f"Error Fetching (delete_from_daycare): {err}")

    def populate_daycare(self):
        try:
            page = self.page_daycare
            selected_item = page.table_care.selectedItems()
            if selected_item and page.button_care_edit.text() == "Enable Edit":
                page.button_care_edit.setText("Cancel")
                page.button_care_details.setEnabled(False)
                day_care_id = int(selected_item[0].text())
                daycare = None
                for care in Day_Care_Service:
                    if care.day_Care_id == day_care_id:
                        daycare = care
                        break
                page.line_care_id.setText(str(daycare.day_care_date))
                page.line_animal_id.setText(str(daycare.animal_id))
                jdate = QDate.fromString(str(daycare.day_care_date), "yyyy-MM-dd")
                page.date_care.setDate(jdate)
                qtime_start = QTime.fromString(str(daycare.start_time), "hh:mm:ss")
                page.time_care_start.setTime(qtime_start)
                qtime_end = QTime.fromString(str(daycare.end_time), "hh:mm:ss")
                page.time_care_end.setTime(qtime_end)
                page.text_care_notes.setPlainText(daycare.notes)

            else:
                page.button_care_edit.setText("Enable Edit")
                self.clear_daycare_fields()
                page.button_care_details.setEnabled(True)
                self.show_daycare()
        except Exception as err:
            print(f"Error Fetching (populate_daycare): {err}")

    def update_daycare(self):
        try:
            page = self.page_daycare
            current_widget = self.stackedWidget.setCurrentWidget(page)
            selected_item = page.table_care.selectedItems()
            if selected_item:
                daycare_id = int(selected_item[0].text())
                day_care_date = page.date_care.text()
                day_care_date_obj = datetime.strptime(
                    str(day_care_date), "%Y-%m-%d"
                ).date()
                Qstart_time = page.time_care_start.time()
                start_time = Qstart_time.toString("hh:mm:ss")
                Qend_time = page.time_care_end.time()
                end_time = Qend_time.toString("hh:mm:ss")

                notes = page.text_care_notes.toPlainText()
                update_daycare_to_db(
                    daycare_id,
                    day_care_date_obj,
                    start_time,
                    end_time,
                    notes,
                )
                self.clear_daycare_fields()
                self.show_daycare()
                page.button_care_details.setEnabled(True)
                page.button_care_edit.setText("Enable Edit")
        except Exception as err:
            print(f"Error Fetching (update_daycare): {err}")

    def set_day_care_table(self):
        try:
            self.page_daycare.table_care.clearContents()
            self.page_daycare.table_care.setRowCount(0)
            fetch_day_care()
            self.page_daycare.table_care.setSortingEnabled(False)
            for row, day_care in enumerate(Day_Care_Service):
                self.add_day_care_to_table(row, day_care)
            self.page_daycare.table_care.setSortingEnabled(True)
        except Exception as err:
            print(f"Error Fetching(set_day_care_table): {err}")

    def add_day_care_to_table(self, row, day_care):
        try:
            header = self.page_daycare.table_care.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            table = self.page_daycare.table_care
            table.insertRow(row)
            """table.setItem(row, 0, QTableWidgetItem(str(day_care.day_Care_id)))
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
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)"""
            table.setItem(row, 0, QTableWidgetItem(str(day_care.day_Care_id)))
            table.setItem(row, 1, QTableWidgetItem(str(day_care.animal_id)))
            table.setItem(row, 2, QTableWidgetItem(str(day_care.day_care_date)))
            table.setItem(row, 3, QTableWidgetItem(str(day_care.start_time)))
            table.setItem(row, 4, QTableWidgetItem(str(day_care.end_time)))
            table.setItem(row, 5, QTableWidgetItem(str(day_care.notes)))
            self.resize_columns_to_contents_alternate2(table)

        except Exception as err:
            print(f"Error Fetching(add_day_care_to_table): {err}")

    ################# Day Care Service End ################

    ###################### Expenses #######################
    def clear_expense_fields(self):
        try:
            page = page = self.page_expenses
            page.line_expense_id.clear()
            page.line_issuer_id.clear()
            page.date_issue.setDate(QDate(2000, 1, 1))
            page.comboBox.setCurrentIndex(0)
            page.date_handle.setDate(QDate(2000, 1, 1))
            page.line_amount.clear()
            page.text_justification.clear()
        except Exception as err:
            print(f"Error clearing expense fields: {err}")

    def get_employee_name_by_id(self, employee_id):
        for employee in Employees:
            if employee.employee_id == employee_id:
                return employee.name
        return None

    def search_expense(self, text):
        try:
            table = self.page_expenses.table_expense
            for row in range(table.rowCount()):
                match = any(
                    text.lower() in table.item(row, col).text().lower()
                    for col in range(table.columnCount())
                )
                table.setRowHidden(row, not match)
        except Exception as err:
            print(f"Error Fetching(search_expense): {err}")

    def populate_expense(self):
        try:
            page = self.page_expenses
            selected_item = page.table_expense.selectedItems()
            if selected_item and page.button_expense_edit.text() == "Enable Edit":
                page.button_expense_edit.setText("Cancel")
                page.button_expense_add.setEnabled(False)
                expense_id = int(selected_item[0].text())
                expense = None
                for ex in Expenses:
                    if ex.expense_id == expense_id:
                        expense = ex
                        break
                page.line_expense_id.setText(str(expense.expense_id))
                page.line_issuer_id.setText(str(expense.issuer_id))
                jdate = QDate.fromString(expense.expense_date, "yyyy-MM-dd")
                page.date_issue.setDate(jdate)
                employee_name = self.get_employee_name_by_id(expense.handler_id)
                if employee_name is not None:
                    employee_info = f"{employee_name} ({expense.handler_id})"
                    page.comboBox.setCurrentText(employee_info)

                jdate2 = QDate.fromString(expense.handle_date, "yyyy-MM-dd")
                page.date_handle.setDate(jdate2)

                page.line_amount.setText(str(expense.amount))
                page.text_justification.setPlainText(expense.justification)
            else:
                page.button_expense_edit.setText("Enable Edit")
                self.clear_expense_fields()
                page.button_expense_add.setEnabled(True)
                self.show_expenses()
        except Exception as err:
            print(f"Error Populating data: {err}")

    def create_new_expense(self):
        try:
            page = self.page_expenses
            current_widget = self.stackedWidget.setCurrentWidget(page)
            issuer_id = page.line_issuer_id.text()
            expense_date = page.date_issue.text()
            expense_date_obj = datetime.strptime(str(expense_date), "%Y-%m-%d").date()
            handler_info = page.comboBox.currentText()
            start_index = handler_info.find("(")
            end_index = handler_info.find(")")
            handler_id = int(handler_info[start_index + 1 : end_index])
            handle_date = page.date_handle.text()
            handle_date_obj = datetime.strptime(str(handle_date), "%Y-%m-%d").date()
            amount = page.line_amount.text()
            justification = page.text_justification.toPlainText()
            if not all(
                [expense_date_obj, handler_id, handle_date, amount, justification]
            ):
                QMessageBox.warning(
                    current_widget, "Warning", "Please fill in all fields."
                )
            mysql_handler = MySQLHandler()
            mysql_handler.connect()
            query = "insert into expenses (handler_id, issuer_id, expense_date, handle_date, amount, justification) values (%s, %s, %s, %s, %s, %s);"
            data = (
                handler_id,
                issuer_id,
                expense_date_obj,
                handle_date,
                amount,
                justification,
            )
            mysql_handler.execute_query(query, data)
            mysql_handler.disconnect()
            QMessageBox.information(current_widget, "Information", "Entry Success!")
            self.clear_expense_fields()
            self.set_expense_table()
        except Exception as err:
            print(f"Insertion failed: {err}")

    def delete_expense(self):
        try:
            page = self.page_expenses
            current_widget = self.stackedWidget.setCurrentWidget(page)
            table = page.table_expense
            selelcted_expense_new = table.currentRow()
            if selelcted_expense_new != -1:
                expense_id = int(table.item(selelcted_expense_new, 0).text())
                table.removeRow(selelcted_expense_new)
                delete_expenses(expense_id)
                QMessageBox.information(
                    current_widget, "Information", "Record deleted successfully!"
                )
            else:
                QMessageBox.warning(
                    current_widget, "Warning", "Select a record to delete!"
                )
        except Exception as err:
            print(f"Deletion Failed: {err}")

    def update_expense(self):
        try:
            page = self.page_expenses
            current_widget = self.stackedWidget.setCurrentWidget(page)
            selected_item = page.table_expense.selectedItems()
            if selected_item:
                expense_id = int(selected_item[0].text())
                issuer_id = page.line_issuer_id.text()
                expense_date = page.date_issue.text()
                expense_date_obj = datetime.strptime(
                    str(expense_date), "%Y-%m-%d"
                ).date()
                print("testing the update expense!")
                handler_info = page.comboBox.currentText()
                start_index = handler_info.find("(")
                end_index = handler_info.find(")")
                handler_id = int(handler_info[start_index + 1 : end_index])

                handle_date = page.date_handle.text()
                handle_date_obj = datetime.strptime(str(handle_date), "%Y-%m-%d").date()
                amount = page.line_amount.text()
                justification = page.text_justification.toPlainText()

                update_expense_to_db(
                    expense_id,
                    issuer_id,
                    handler_id,
                    expense_date_obj,
                    handle_date_obj,
                    amount,
                    justification,
                )
                self.clear_expense_fields()
                self.show_expenses()
                page.button_expense_edit.setText("Enable Edit")
                page.button_expense_add.setEnabled(True)
            else:
                QMessageBox.warning(
                    current_widget, "Warning", "Select a record to edit!"
                )
        except Exception as err:
            print(f"Update Failed: {err}")

    def set_expense_table(self):
        try:
            self.page_expenses.table_expense.clearContents()
            self.page_expenses.table_expense.setRowCount(0)
            fetch_expenses()
            self.page_expenses.table_expense.setSortingEnabled(False)
            for row, expense in enumerate(Expenses):
                self.add_expense_to_table(row, expense)
            self.page_expenses.table_expense.setSortingEnabled(True)
        except Exception as err:
            print(f"Error Fetching(set_expense_table): {err}")

    def add_expense_to_table(self, row, expense):
        try:
            # print("Testing add_expense to table")
            table = self.page_expenses.table_expense
            table.insertRow(row)

            table.setItem(row, 0, QTableWidgetItem(str(expense.expense_id)))
            table.setItem(row, 1, QTableWidgetItem(str(expense.issuer_id)))
            table.setItem(row, 2, QTableWidgetItem(str(expense.handler_id)))
            table.setItem(row, 3, QTableWidgetItem(str(expense.expense_date)))
            table.setItem(row, 4, QTableWidgetItem(str(expense.handle_date)))
            table.setItem(row, 5, QTableWidgetItem(str(expense.amount)))
            table.setItem(row, 6, QTableWidgetItem(str(expense.justification)))

            self.resize_columns_to_contents_alternate2(table)
        except Exception as err:
            print(f"Error Fetching(add_expense_to_table): {err}")

    ################### Expense End #####################

    ##################### Billing #######################
    def search_bill(self, text):
        try:
            table = self.page_billing.table_bill
            for row in range(table.rowCount()):
                match = any(
                    text.lower() in table.item(row, col).text().lower()
                    for col in range(table.columnCount())
                )
                table.setRowHidden(row, not match)
        except Exception as err:
            print(f"Error Fetching(search_bill): {err}")

    '''def add_new_bill(self):
        try:
            page = self.page_billing
            current_widget = self.stackedWidget.setCurrentWidget(page)
            animal_id = page.line_animal_id.text()
            # other_expenses = page.line_other_expenses.

        except Exception as err:
            print(f"Error Fetching(add_new_bill): {err}")'''

    def populate_bill(self):
        try:
            ...
        except Exception as err:
            print(f"Error Fetching(populate_bill): {err}")

    def delete_bill(self):
        try:
            ...
        except Exception as err:
            print(f"Error Fetching(delete_bill): {err}")

    def update_bill(self):
        try:
            ...
        except Exception as err:
            print(f"Error Fetching(update_bill): {err}")

    def set_bill_table(self):
        try:
            self.page_billing.table_bill.clearContents()
            self.page_billing.table_bill.setRowCount(0)
            fetch_billings()
            self.page_billing.table_bill.setSortingEnabled(False)
            for row, billing in enumerate(Billings):
                self.add_billing_to_table(row, billing)

                service_details = self.get_service_details(billing.services, Services)
                self.page_billing.table_show_service.setSortingEnabled(False)
                for rowService, service in enumerate(service_details):
                    self.add_billing_service_to_service_table(rowService, service)
                self.page_billing.table_show_service.setSortingEnabled(True)
            self.page_billing.table_bill.setSortingEnabled(True)
        except Exception as err:
            print(f"Error Fetching(set_bill_table): {err}")

    def get_service_details(self, service_ids, services):
        try:
            return [
                service for service in services if service.service_id in service_ids
            ]
        except Exception as err:
            print(f"Error Fetching(get_service_details): {err}")

    def add_billing_to_table(self, row, billing):
        try:
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
            table.setItem(row, 3, QTableWidgetItem(str(billing.billing_date)))
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            table.setItem(row, 4, QTableWidgetItem(str(billing.total_amount)))
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
            table.setItem(row, 5, QTableWidgetItem(str(billing.adjustment)))
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
            table.setItem(row, 6, QTableWidgetItem(str(billing.status)))
            header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
            """self.resize_columns_to_contents_alternate(table)
                table.resizeColumnToContents(0)
                table.resizeColumnToContents(1)
                table.resizeColumnToContents(2) """
        except Exception as err:
            print(f"Error Fetching(add_billing_to_table): {err}")

    def add_billing_service_to_service_table(self, rowService, service):
        try:
            header = self.page_billing.table_show_service.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

            table = self.page_billing.table_show_service

            table.setItem(rowService, 0, QTableWidgetItem(service.service_id))
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)

            table.setItem(rowService, 1, QTableWidgetItem(service.name))
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

            table.setItem(rowService, 2, QTableWidgetItem(service.cost))
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        except Exception as err:
            print(f"Error Fetching(add_billing_service_to_service_table): {err}")

    #################### End Billing ####################

    #################### Appointment ####################
    def search_appointment(self, text):
        try:
            table = self.page_appointment.appointment_table_widget_2
            for row in range(table.rowCount()):
                match = any(
                    text.lower() in table.item(row, col).text().lower()
                    for col in range(table.columnCount())
                )
                table.setRowHidden(row, not match)
        except Exception as err:
            print(f"Error Fetching(search_appointment): {err}")

    def checkbox_state_changed(self, state):
        try:
            combo_box = self.page_appointment_create.comboBox_animal_id
            if state == 0:
                combo_box.setEnabled(True)
                animal_info = [
                    f"{animal.species}, {animal.owner_name} ({animal.animal_id})"
                    for animal in Animals
                ]
                animal_info.insert(0, "Select")
                combo_box.addItems(animal_info)
                combo_box.completer().setCompletionMode(
                    QtWidgets.QCompleter.PopupCompletion
                )
            else:
                combo_box.clear()
                combo_box.setEnabled(False)

        except Exception as err:
            print(f"Error Fetching(checkbox_state_changed): {err}")

    """def get_animal_by_id(self, animal_id):
        try:
            for animal in Animals:
                if animal.animal_id == animal_id:
                    return animal
            return None

        except Exception as err:
            print(f"Error Fetching(get_animal_by_id): {err}")"""

    def set_appointment_table(self):
        try:
            self.page_appointment.appointment_table_widget_2.clearContents()
            self.page_appointment.appointment_table_widget_2.setRowCount(0)
            fetch_appointment()
            self.page_appointment.appointment_table_widget_2.setSortingEnabled(False)
            for row, appointment in enumerate(Appointments):
                # animal = self.get_animal_by_id(appointment.animal_id)
                # self.add_appointment_to_Table(row, appointment, animal)
                self.add_appointment_to_Table(row, appointment)
            self.page_appointment.appointment_table_widget_2.setSortingEnabled(True)

        except Exception as err:
            print(f"Error Fetching(set_appointment_table): {err}")

    def add_appointment_to_Table(self, row, appointment):
        try:
            header = self.page_appointment.appointment_table_widget_2.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            table = self.page_appointment.appointment_table_widget_2
            table.insertRow(row)

            table.setItem(row, 0, QTableWidgetItem(str(appointment.appointment_id)))
            table.setItem(row, 1, QTableWidgetItem(str(appointment.animal_id)))
            table.setItem(row, 2, QTableWidgetItem(appointment.owner_name))
            table.setItem(row, 3, QTableWidgetItem(appointment.phone_number))
            table.setItem(row, 4, QTableWidgetItem(appointment.species))
            table.setItem(row, 5, QTableWidgetItem(appointment.visit_reason))
            table.setItem(row, 6, QTableWidgetItem(str(appointment.appointment_date)))
            table.setItem(row, 7, QTableWidgetItem(str(appointment.appointment_time)))
            table.setItem(row, 8, QTableWidgetItem(appointment.appointment_status))

            self.resize_columns_to_contents(table, header)

        except Exception as err:
            print(f"Error Fetching(add_appointment_to_Table): {err}")

    def create_appointment(self):
        try:
            new_animal: bool = False
            day_care: bool = False

            page = self.page_appointment_create
            current_widget = self.stackedWidget.setCurrentWidget(page)

            if page.chk_box_new_animal.isChecked():
                new_animal = True

                animal_name = page.comboBox_animal_id.currentItem()
                birth_date = page.date_appt_birth.Text()

                gender = ""
                if page.rb_male.isChecked():
                    gender = "Male"
                elif page.rb_female.isChecked():
                    gender = "Female"

                sterilized = ""
                if page.rb_ster_yes.isChecked():
                    sterilized = "Yes"
                elif page.rb_ster_yes.isChecked():
                    sterilized = "No"

                species = page.line_species.Text()
                breed = page.line_breed.Text()
                color = page.line_colors.Text()
                behavioral_warning = page.line_behave.Text()
                owner_name = page.line_o_fname.Text() + " " + page.line_o_lname.Text()
                email = page.line_email.Text()
                phone = page.line_phone.Text()
                address = page.line_address.Text()
                reg_date = page.date_appt_reg.Text()
                med_condition = page.line_reason.Text()

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
                    QMessageBox.warning(
                        current_widget, "Warning", "Please fill in all fields."
                    )
                return
                animal_id = add_animal(
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
                    med_condition,
                )
                # there's your id, continue the work ;-;
                # How do i get animal id for appointment table? I just inserted the new animal in database
                # Even if I fetch animal list, how will I get our desired animal id?
                ...

            else:
                ...

            if page.chk_box_day_care.isChecked():
                day_care = True
                ...

            else:
                ...

            self.show_appointment
        except Exception as err:
            print(f"Error Fetching(create_appointment): {err}")

    def update_existing_appointment(self):
        try:
            page = self.page_appointment_modify
            current_widget = self.stackedWidget.setCurrentWidget(page)

            self.show_appointment

        except Exception as err:
            print(f"Error Fetching(update_existing_appointment): {err}")

    def delete_existing_appointment(self):
        try:
            page = self.page_appointment

        except Exception as err:
            print(f"Error Fetching(delete_existing_appointment): {err}")

    ################## Appointment End ####################

    ################## Service Start ##################
    def clear_service_fields(self):
        try:
            page = self.page_service
            page.line_service_id.clear()
            page.line_service_name.clear()
            page.line_service_cost.clear()
            page.pte_service_details.clear()
            # page.buttoGroup.setExclusive(False)
            page.rb_service_available.setChecked(True)
            page.rb_service_unavailable.setChecked(False)
            # page.buttoGroup.setExclusive(True)

        except Exception as err:
            print(f"Error(clear_service_fields): {err}")

    def set_service_table(self):
        try:
            self.page_service.table_service.clearContents()
            self.page_service.table_service.setRowCount(0)
            fetch_services()
            self.page_service.table_service.setSortingEnabled(False)
            for row, service in enumerate(Services):
                self.add_services_to_table(row, service)
            self.page_service.table_service.setSortingEnabled(True)

        except Exception as err:
            print(f"Error (set_service_table): {err}")

    def add_services_to_table(self, row, service):
        try:
            table = self.page_service.table_service
            header = table.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

            table.insertRow(row)

            table.setItem(row, 0, QTableWidgetItem(str(service.service_id)))
            # header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            table.setItem(row, 1, QTableWidgetItem(service.name))
            # header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            table.setItem(row, 2, QTableWidgetItem(str(service.cost)))
            # header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            table.setItem(row, 3, QTableWidgetItem(str(service.service_availability)))
            # header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            table.setItem(row, 4, QTableWidgetItem(service.service_details))
            # header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)

            self.resize_columns_to_contents_alternate2(table)

        except Exception as err:
            print(f"Error (add_service_to_table): {err}")

    def populate_service(self):
        try:
            # service = None
            selected_item = self.page_service.table_service.selectedItems()
            # service = None
            if (
                selected_item
                and self.page_service.button_service_cancel.text() == "Enable Edit"
            ):
                self.page_service.button_service_cancel.setText("Cancel Edit")
                self.page_service.button_service_add.setEnabled(False)
                service_id = int(selected_item[0].text())
                service = None
                for srv in Services:
                    if srv.service_id == service_id:
                        service = srv
                        break

                page = self.page_service

                page.line_service_id.setText(str(service.service_id))
                page.line_service_name.setText(service.name)
                page.line_service_cost.setText(str(service.cost))

                if (
                    service.service_availability.lower() == "true"
                    or service.service_availability.lower() == "yes"
                ):
                    page.rb_service_available.setChecked(True)
                    page.rb_service_unavailable.setChecked(False)
                elif (
                    service.service_availability.lower() == "false"
                    or service.service_availability.lower() == "no"
                ):
                    page.rb_service_available.setChecked(False)
                    page.rb_service_unavailable.setChecked(True)

                page.pte_service_details.setPlainText(service.service_details)

            else:
                self.page_service.button_service_cancel.setText("Enable Edit")
                self.clear_service_fields()
                self.page_service.button_service_add.setEnabled(True)
                self.show_service()
        except Exception as err:
            print(f"Error Fetching(populate_service): {err}")

    def add_new_service(self):
        try:
            page = self.page_service
            current_widget = self.stackedWidget.setCurrentWidget(page)
            name = page.line_service_name.text()
            cost = float(page.line_service_cost.text())
            details = page.pte_service_details.toPlainText()
            if page.rb_service_available.isChecked():
                availability = "Yes"
            elif page.rb_service_unavailable.isChecked():
                availability = "No"

            if not all([name, cost, availability, details]):
                QMessageBox.warning(
                    current_widget, "Warning! Please fill in all fields."
                )
                return

            add_service(name, cost, details, availability)
            self.clear_service_fields()
            self.show_service()

        except Exception as err:
            print(f"Error Fetching(add_new_service): {err}")

    def update_existing_service(self):
        try:
            selected_item = self.page_service.table_service.selectedItems()
            if selected_item:
                service_id = int(selected_item[0].text())

                page = self.page_service

                name = page.line_service_name.text()
                cost = float(page.line_service_cost.text())
                details = page.pte_service_details.toPlainText()
                if page.rb_service_available.isChecked():
                    availability = "Yes"
                elif page.rb_service_unavailable.isChecked():
                    availability = "No"

                update_service(service_id, name, cost, details, availability)
                self.clear_service_fields()
                self.show_service()
                self.page_service.button_service_add.setEnabled(True)
                self.page_service.button_service_cancel.setText("Enable Edit")
            else:
                print("Select a Row!")
        except Exception as err:
            print(f"Error Fetching(update_existing_service): {err}")

    def delete_existing_service(self):
        try:
            page = self.page_service
            table = page.table_service
            current_widget = self.stackedWidget.setCurrentWidget(page)
            selected_service_row = table.currentRow()

            if selected_service_row != -1:
                service_id = int(table.item(selected_service_row, 0).text())
                table.removeRow(selected_service_row)
                delete_service(service_id)

            else:
                QMessageBox.warning(current_widget, "Warning! Select a row to delete.")

        except Exception as err:
            print(f"Service Delete Failed!: {err}")

    ################## Service End ####################

    ############### Table Resize Methods ##################
    def resize_columns_to_contents_alternate(self, table):
        try:
            header = table.horizontalHeader()

            for column in range(table.columnCount()):
                max_width = header.sectionSizeHint(column)

                for row in range(table.rowCount()):
                    item = table.item(row, column)
                    if item is not None and item.text():
                        max_width = max(
                            max_width, table.fontMetrics().width(item.text()) + 10
                        )

                header.setSectionResizeMode(column, max_width)
        except Exception as err:
            print(f"Error Stretching: {err}")

    def resize_columns_to_contents(self, table, header):
        try:
            for column in range(table.columnCount()):
                max_width = header.sectionSizeHint(column)

                for row in range(table.rowCount()):
                    item = table.item(row, column)
                    if item is not None and item.text():
                        max_width = max(
                            max_width, table.fontMetrics().width(item.text()) + 10
                        )

                header.resizeSection(column, max_width)
        except Exception as err:
            print(f"Error Fetching: {err}")

    def resize_columns_to_contents_alternate2(self, table):
        try:
            header = table.horizontalHeader()

            for column in range(table.columnCount()):
                max_width = header.sectionSizeHint(column)

                for row in range(table.rowCount()):
                    item = table.item(row, column)
                    if item is not None and item.text():
                        max_width = max(
                            max_width, table.fontMetrics().width(item.text()) + 10
                        )

                header.setSectionResizeMode(column, QtWidgets.QHeaderView.Interactive)
                header.resizeSection(column, max_width)
        except Exception as err:
            print(f"Error Stretching: {err}")

    ############### Table Resize Methods End ################


#### UI density Scaling modifier ####
extra = {
    # Density Scale
    "density_scale": "-2",
}
if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    # window.show()
    with open("config.txt", "r") as f:
        read = f.read()
        if not read:
            read = "dark_medical.xml"
        apply_stylesheet(app, theme=read, extra=extra)
        window.page_setting.comboBox_themes.setCurrentText(read)
    # apply_stylesheet(app, theme='light_blue.xml', css_file='custom.css')
    window.adjustSize()
    window.showMaximized()
    # window.showFullScreen()
    sys.exit(app.exec_())
