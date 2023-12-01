import MySQLHandler
import Appointment
import Animal
import Billing
import Employee
import Expenses
import Inventory
import Service
import Veterinarian
from datetime import date
###Animal#
Animals=[]
user = "root"
password = "root"
host = "localhost"
def fetch_animals():   
    try:
        mysql_handler = MySQLHandler(host, user, password)
        mysql_handler.connect()     
        query = "select * from animals"
        data = mysql_handler.execute_query(query)
        for row in data:
            animal = Animal(row[1], row[2], row[3], row[4], row, [5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
            animal.animal_id(row[0])
            Animals.append(animal)
    except Exception as err:
        print(f"Error: {err}")
    finally: mysql.close()
        
def add_animal(animal_name:str, birth_date:str, 
                    sterilized:bool, gender:str, species:str, breed:str, 
                    color:str, behavioral_warning:str, 
                    owner_name:str, email:str, phone:str, address:str, med_condition:str = None):
    try:
        reg_date = date.today()
        new_animal = Animal(animal_name, birth_date, sterilized, gender, species, breed,
                            color, behavioral_warning, owner_name, email, phone, address, currentDate, med_condition)
        Animals.append(new_animal)
        
        query = "insert into animal (animal_name, birth_date, sterilized, gender, species, breed, color, behavioral_warning, owner_name, email, phone, address, reg_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (animal_name, birth_date, sterilized, gender, species, breed, color, behavioral_warning, owner_name, email, phone, address, reg_date)
        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        mysql_handler.execute_query(query, values)
        return "Entry Success!"
    except Exception as err:
        return "Entry Failed!"
    finally:
        mysql_handler.disconnect()
    
def delete_animal(id:int):
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
def add_appointment(date, time, reason:str, name:str, phone:str, address:str, animal_name:str, species:str, breed:str,
                              color:str, behaviour:str, birth:str, reg_date:str):
    apt = Appointment(date, time, re)

### Employee ###
Employee = []

def add_employee(name: str, email: str, password: str, address: str, access_level: int,
                working_hours: str, designation: str, salary: float, joining_date: str, phone:str = []):
    try:
        mysql_handler = MySQLHandler(host, user, password)
        mysql_handler.connect()
        new_employee = Employee(name, email, password, address, access_level, working_hours, designation, salary, joining_date, phone)
        Employee.append(new_employee)

        query = "insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date) values(%s, %s, %s, %s, %s, %s, %s, %s,%s);"
        data  = values(name, email, password, address, designation, access_level, working_hours, salary, joining_date)
        mysql_handler.execute_query(query, data)
        query = "insert into phone (id, phone_number) values(%s, %s);"
        query_fetch_id = "select id from employee order by id desc limit 1;"
        row = mysql_handler.fetch_data(query_fetch_id)
        id = row[0]
        #data = values(row[0][0], phone)
        data1 = values(id, phone[0])
        data2 = values(id, phone[1])
        mysql_handler.execute_query(query, data1)
        mysql_handler.execute_query(query, data2)
    except Exception as err: 
        print(f"Error: {err}")
    finally:
        mysql_handler.disconnect()
    
### Services List For Billing###
Services = []






###### Inventory#####
Inventory =[]

def add_inventory ():...