from MySQLHandler import MySQLHandler

user = "root"
password = "1234"
host = "localhost"
port = 3307
class Appointment:
    def __init__(
        self,
        animal_id: int,
        appointment_date: str,
        appointment_time: str,
        visit_reason: str,
        appointment_status: str,
    ):
        self.appointment_id = None
        self.animal_id = animal_id
        self.owner_name = None
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.visit_reason = visit_reason
        self.appointment_status = appointment_status

    ########getter, setter###########
    @property
    def appointment_id(self):
        return self._appointment_id

    
    @appointment_id.setter
    def appointment_id(self, appointment_id: int):
        self._appointment_id = appointment_id
    

    @property
    def animal_id(self):
        return self.animal_id

    @animal_id.setter
    def animal_id(self, animal_id: int):
        self._animal_id = animal_id

    @property
    def appointment_date(self):
        return self._appointment_date

    @appointment_date.setter
    def appointment_date(self, appointment_date: str):
        self._appointment_date = appointment_date

    @property
    def appointment_time(self):
        return self._appointment_time

    @appointment_time.setter
    def appointment_time(self, appointment_time: str):
        self._appointment_time = appointment_time

    @property
    def visit_reason(self):
        return self._visit_reason

    @visit_reason.setter
    def visit_reason(self, visit_reason: str):
        self._visit_reason = visit_reason

    @property
    def appointment_status(self):
        return self._appointment_status

    @appointment_status.setter
    def appointment_status(self, appointment_status: str):
        self._appointment_status = appointment_status
    ########getter, setter end###########

###  Appointment #####
Appointments = []

def fetch_appointment():
    try:
        mysql_handler = MySQLHandler(host, user, password, port)
        mysql_handler.connect()
        query = "select * from appointment;"
        data = mysql_handler.fetch_data(query)

        for row in data:
            appointment = Appointment(
                animal_id=int(row[1]),
                appointment_date=str(row[2]),
                appointment_time=str(row[3]),
                visit_reason=row[4],
                appointment_status=row[5]
            )
            appointment.appointment_id = int(row[0])
            Appointments.append(appointment)
        mysql_handler.disconnect()
        print(f"Er")
    except Exception as err:
        print(f"Entry Failed!:{err}") 

def add_appointment(
    animal_id: int,
    appointment_date: str,
    appointment_time: str,
    visit_reason: str,
    appointment_status: str  
):
    try:
        new_appointment = Appointment(
            animal_id,
            appointment_date,
            appointment_time,
            visit_reason,
            appointment_status
        )
        Appointments.append(new_appointment)

        query = "insert into appointments(animal_id, appointment_date, appointment_time, visit_reason, appointment_status) values(%s, %s, %s, %s, %s)"
        values = (animal_id, 
                    appointment_date, 
                    appointment_time, 
                    visit_reason, 
                    appointment_status
                    )
        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        mysql_handler.execute_query(query, values)
        mysql_handler.disconnect()
        print("Entry Success!")

    except Exception as err:
        print(f"Entry Failed!:{err}") 

def delete_appointment(id:int):
    try:
        for appointment in Appointments: 
            if id == appointment_id:
                mysql_handler = MySQLHandler(host, user, password, port)
                mysql_handler.connect()
                query = "delete from appointments where id = %s;"
                data = appointment.id
                mysql_handler.execute_query(query, data)
                Appointments.remove(appointment)
        mysql_handler.disconnect()
        print("Delete Success!")
        print("Delete Failed!")
    except Exception as err:
        print(f"Error: {err}")