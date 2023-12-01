import MysqlConnectionManager as mysql
import Appointment
import Animal
import Billing
import Employee
import Expenses
import Item
import Service
import Veterinarian
from datetime import date
###Animal#
Animals=[]
def fetch_animals():
    mysql.connect()
    que = "select animal_id, animal_name, birth_date, sterilized, gender, species, breed, color, behavioral_warning, owner_name, email, phone, address, reg_date"
    query()
        
def add_animal(animal_name:str, birth_date:str, 
                    sterilized:bool, gender:str, species:str, breed:str, 
                    color:str, behavioral_warning:str, 
                    owner_name:str, email:str, phone:str, address:str, med_condition:str = None):
    try:
        currentDate = date.today()
        new_animal = Animal(animal_name, birth_date, sterilized, gender, species, breed,
                            color, behavioral_warning, owner_name, email, phone, address, currentDate, med_condition)
        Animals.append(new_animal)
        mysql.connect()
        que = "insert into animal (name, species, breed, color, gender, birth_date, sterilized, current_condition, behavioral_warning, oname, email,phone, address, reg_date)"
        data = f"values({animal_name, species, breed, color, gender, birth_date, sterilized, med_condition, behavioral_warning, owner_name, email, phone, address, currentDate});"
        query(que, data)
        mysql.close()
        return "Entry Success!"
    except Exception as err:
        return "Entry Failed!"
    
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
        new_employee = Employee(name, email, password, address, access_level,working_hours, designation, salary, joining_date, phone)
        Employee.append(new_employee)
        mysql.connect()
        que = "insert into employees (name, email, password, address, access_level,working_hours, designation, salary, joining_date)"
        data  = "values()"
        query(que, data)
        #que = 
        #que
    except:
        ...
    
### Services List For Billing###
Services = []






###### Item add and delete #####
Items =[]

def add_item (mng_id:int, name:str,manufacturer:str, item_type:str, price:float, amount:int):

    try:
        new_item = Item(mng_id,name,manufacturer,item_type,price,amount)
        Items.append(new_item)
        mysql.connect()
        que ="insert into item (mng_id,name, manufacturer, item_type,price,amount)"
        data = f"values({mng_id,name, manufacturer, item_type,price,amount})"
        query (que+data)
        mysql.close()
        return "Entry success"
    except Exception as err:
         return "Entry failed"

def remove_item (id:int):
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