from MySQLHandler import MySQLHandler
import Appointment
from Animal import Animal
from Billing import Bill
import Employee
import Expenses
import Item
import Service

user = "root"
password = "1234"
host = "localhost"
port = 3307

# import Veterinarian
from datetime import date

###Animal#
Animals: Animal = []


def fetch_animals():
    try:
        mysql_handler = MySQLHandler(host, user, password, port)
        mysql_handler.connect()
        query = "select * from animals"
        data = mysql_handler.fetch_data(query)

        for row in data:
            animal = Animal(
                animal_name=row[1],
                birth_date=str(row[2]),
                sterilized=str(row[3]),
                gender=row[4],
                species=row[5],
                breed=row[6],
                color=row[7],
                behavioral_warning=row[8],
                owner_name=row[9],
                email=row[10],
                phone=row[11],
                address=row[12],
                reg_date=str(row[13]),
                med_condition=row[14],
            )
            animal.animal_id = int(row[0])
            # query = "select * from records where animal_id = %s"
            # value = animal.animal_id
            # data = mysql_handler.fetch_data(query, value)
            """
            for rec in data:
                print(rec)               
                animal.add_record(record_id=rec[0], record=str(rec[2]), date=str(rec[3]))
            """
            Animals.append(animal)
        mysql_handler.disconnect()
        print(f"Er")
    except Exception as err:
        print(f"Error Fetching: {err}")


def add_animal(
    animal_name: str,
    birth_date: str,
    sterilized: bool,
    gender: str,
    species: str,
    breed: str,
    color: str,
    behavioral_warning: str,
    owner_name: str,
    email: str,
    phone: str,
    address: str,
    med_condition: str = None,
):
    try:
        reg_date = date.today()
        new_animal = Animal(
            animal_name,
            birth_date,
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
            currentDate,
            med_condition,
        )
        Animals.append(new_animal)

        query = "insert into animal (animal_name, birth_date, sterilized, gender, species, breed, color, behavioral_warning, owner_name, email, phone, address, reg_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
            animal_name,
            birth_date,
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
            reg_date,
        )
        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        mysql_handler.execute_query(query, values)
        return "Entry Success!"
        mysql_handler.disconnect()
    except Exception as err:
        return "Entry Failed!"
        


def delete_animal(id: int):
    try:
        for animal in Animals:
            if id == animal.id:
                mysql.connect()
                run_query(f"delete from animal where id = {animal.id}")
                Animals.remove(animal)
                mysql.close()
                return "Delete Success!"
        return "Delete Failed!"
    except Exception as err:
        print(f"Error: {err}")


###  Appointment #####
def add_appointment(
    date,
    time,
    reason: str,
    name: str,
    phone: str,
    address: str,
    animal_name: str,
    species: str,
    breed: str,
    color: str,
    behaviour: str,
    birth: str,
    reg_date: str,
):
    apt = Appointment(date, time, re)


### Employee ###
Employee = []
def fetch_employees():
    try:
        mysql_handler = MySQLHandler(host, user, password, port)
        mysql_handler.connect()
        query = "select * from employees;"
        data = mysql_handler.fetch_data(query)
    except:
        pass

def add_employee(
    name: str,
    email: str,
    password: str,
    address: str,
    access_level: int,
    working_hours: str,
    designation: str,
    salary: float,
    joining_date: str,
    phone: str = [],
):
    try:
        new_employee = Employee(
            name,
            email,
            password,
            address,
            access_level,
            working_hours,
            designation,
            salary,
            joining_date,
            phone,
        )
        Employee.append(new_employee)

        query = "insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date) values(%s, %s, %s, %s, %s, %s, %s, %s,%s);"
        data = values(
            name,
            email,
            password,
            address,
            designation,
            access_level,
            working_hours,
            salary,
            joining_date,
        )

        mysql_handler = MySQLHandler(host, user, password)
        mysql_handler.connect()
        mysql_handler.execute_query(query, data)
        query = "insert into phone (id, phone_number) values(%s, %s);"
        query_fetch_id = "select id from employee order by id desc limit 1;"
        row = mysql_handler.fetch_data(query_fetch_id)
        id = row[0]
        # data = values(row[0][0], phone)
        data1 = values(id, phone[0])
        data2 = values(id, phone[1])
        mysql_handler.execute_query(query, data1)
        mysql_handler.execute_query(query, data2)       
        mysql_handler.disconnect()
        print("Entry Success!")
    except Exception as err:
        print("Entry Failed: {err}")
        

### Billing ####
Billings = []

def fetch_billings():
    try:
        mysql_handler = MySQLHandler(host, user, password, port)
        mysql_handler.connect()
        query = "select * from billings;"
        data = mysql_handler.fetch_data(query)
        query = "select * from bill_services;"
        dataServices = mysql_handler.fetch_data(query)

        for row in data:
            billing = Bill(
                day_care_id=int(row[1]),
                appointment_id=int(row[2]),
                payment_date=str(row[3]),
                total_amount=float(row[4]),
                adjustment=float(row[5]),
                status=row[6],
            )
            billing.billing_id = int(row[0])

            for rowServices in dataServices:
                if billing.billing_id == rowServices[0]:
                    billing.add_services(rowServices[1])

            Billings.append(billing)
        mysql_handler.disconnect()
    except Exception as err:
        print(f"Error Fetching: {err}")

def add_bill(
    day_care_id:int,
    appointment_id:int,
    payment_date:str,
    total_amount:float,
    adjustment:float,
    status:str
):
    try:
        payment_date = date.today()
        new_bill = Bill(
            day_Care_id,
            appointment_id,
            currentDate,
            total_amount,
            adjustment,
            status
        )
        Billings.append(new_bill)

        query = "insert into animal (day_care_id, appointment_id, payment_date, total_amount, adjustment, status) values(%s,%s,%s,%s,%s,%s)"
        values = (
            day_care_id,
            appointment_id,
            payment_date,
            total_amount,
            adjustment,
            status
        )
        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        mysql_handler.execute_query(query, values)
        return "Entry Success!"
        mysql_handler.disconnect()
    except Exception as err:
        return "Entry Failed!"

def delete_bill(id:int):
    try:
        for bill in Billings:
            if id == billing.billing_id:
                mysql.connect()
                run_query(f"delete from billings where id = {billing.id}")
                Billings.remove(billing)
                mysql.close()
                return "Delete Success!"
        return "Delete Failed!"
    except Exception as err:
        print(f"Error: {err}")
### End Billing ####

### Services List For Billing###
Services = []

def fetch_services():
    try:
        mysql_handler = MySQLHandler(host, user, password, port)
        mysql_handler.connect()
        query = "select * from services"
        data = mysql_handler.fetch_data(query)

        for row in data:
            services = Services(
                name=row[1],
                cost=float(row[2]),
                service_details=row[3],
                service_availability=bool(row[4]),
            )
            services.service_id = int(row[0])
            Services.append(services)
        mysql_handler.disconnect()
    except Exception as err:
        print(f"Error Fethcing: {err}")

def add_service(
    name:str,
    cost:float,
    service_details:str,
    service_availability:bool
):
    try:
        new_service = Service(
            name,
            cost,
            service_details,
            service_availability
        )
        Services.append(new_service)

        query = "insert into services (name, cost, service_details, service_availibility) values(%s,%s,%s,%s)"
        values = (
            name,
            cost,
            service_details,
            service_availability
        )
        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        mysql_handler.execute_query(query, values)
        return "Entry Success!"
        mysql_handler.disconnect()
    except Exception as err:
        return "Entry Failed!"

def delete_service(id:int):
    try:
        for service in Services:
            if id == service.id:
                mysql.connect()
                run_query(f"delete from service where id = {service.id}")
                Services.remove(service)
                mysql.close()
                return "Delete Success!"
        return "Delete Failed!"
    except Exception as err:
        print(f"Error: {err}")
### End Services List For Billing###

###### Item add and delete #####
Items = []

def fetch_items():
    try:
        mysql_handler = MySQLHandler(host, user, password)
        mysql_handler.connect()
        query = "select * from inventory"
        data = mysql_handler.fetch_data(query)

        for row in data:
            item = Item(
                name=row[1],
                manufacturer=str(row[2]),
                item_type=str(row[3]),
                price=row[4],
                amount=row[5],
            )
            item.item_id = int(row[0])
            Items.append(item)
        mysql_handler.disconnect()
        print(f"Er")
    except Exception as err:
        print(f"Error Fetching: {err}")

def add_item(name: str, manufacturer: str, item_type: str, price: float, amount: int):
    try:
        new_item = Item(mng_id, name, manufacturer, item_type, price, amount)
        Items.append(new_item)
        query = "insert into item (name, manufacturer, item_type,price,amount)"
        values = (name, manufacturer, item_type, price, amount)
        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        mysql_handler.execute_query(query, values)
        return "Entry success"
    except Exception as err:
        return "Entry failed"

def remove_item(id: int):
    try:
        for item in Items:
            if id == item.id:
                mysql.connect()
                run_query(f"Delete from item where id= {item.id}")
                Items.remove(item)
                mysql.close()
                return "Delete success!"
    except Exception as err:
        print(f"Error: {err}")
