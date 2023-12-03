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
password = "1234"
host = "localhost"
port = 3307
port = 3307

# import Veterinarian
from datetime import date



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

