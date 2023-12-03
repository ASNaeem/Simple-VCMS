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
