import MysqlConnectionManager as db
import Appointment
def add_appointment_db(date, time, reason:str, name:str, phone:str, address:str, animal_name:str, species:str, breed:str,
                              color:str, behaviour:str, birth:str, reg_date:str):
    apt = Appointment(date, time, re)
    
    cursor = db.establish_connection()
    cursor.execute("insert into appointment()")

