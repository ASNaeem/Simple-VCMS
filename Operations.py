import MysqlConnectionManager as mysql
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
def add_animal(animal_id:int, animal_name:str, birth_date:str, 
                    sterilized:bool, gender:str, species:str, breed:str, 
                    color:str, behavioral_warning:str, 
                    owner_name:str, email:str, phone:str, address:str, med_condition:str = None):
    try:
        currentDate = date.today()
        new_animal = Animal(animal_id, animal_name, birth_date, sterilized, gender, species, breed,
                            color, behavioral_warning, owner_name, email, phone, address, currentDate, med_condition)
        Animals.append(new_animal)
        mysql.connect()
        query = "insert into animal (name, species, breed, color, gender, birth_date, sterilized, current_condition, behavioral_warning, oname, email,phone, address, reg_date)"
        data = f" values ({animal_name, species, breed, color, gender, birth_date, sterilized, med_condition, behavioral_warning, owner_name, email, phone, address, currentDate});"
        run_query(query+data)
        mysql.close()
        return "Entry Success!"
    except Exception as err:
        return "Entry Failed!"
    

def run_query(query:str, data=None):
    cursor(query)
    
def delete_animal(id:int):
    for animal in Animals:
        if id == animal.id:
            mysql.connect()
            run_query(f"delete from animal where id = {animal.id}")
            Animals.remove(animal)
            mysql.close()
            return "Delete Success!"
    return "Delete Failed!"
###  Appointment #####

def add_appointment_db(date, time, reason:str, name:str, phone:str, address:str, animal_name:str, species:str, breed:str,
                              color:str, behaviour:str, birth:str, reg_date:str):
    apt = Appointment(date, time, re)
    
    

