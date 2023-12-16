from MySQLHandler import MySQLHandler


class Appointment:
    def __init__(
        self,
        animal_id: int,
        vet_id: int,
        owner_name: str,
        phone_number: str,
        species: str,
        appointment_date: str,
        appointment_time: str,
        visit_reason: str,
        appointment_status: str = "Scheduled",
    ):
        self.appointment_id = None
        self.animal_id = animal_id
        self.vet_id = vet_id
        self.owner_name = owner_name
        self.phone_number = phone_number
        self.species = species
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
        return self._animal_id
    @animal_id.setter
    def animal_id(self, animal_id: int):
        self._animal_id = animal_id

    @property
    def vet_id(self):
        return self._vet_id
    @vet_id.setter
    def vet_id(self, vet_id: int):
        self._vet_id = vet_id

    @property
    def owner_name(self):
        return self._owner_name
    @owner_name.setter
    def owner_name(self, owner_name: str):
        self._owner_name = owner_name

    @property
    def phone_number(self):
        return self._phone_number
    @phone_number.setter
    def phone_number(self, phone_number: str):
        self._phone_number = phone_number

    @property
    def species(self):
        return self._species
    @species.setter
    def species(self, species: str):
        self._species = species

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
        Appointments.clear()
        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        query = "select ap.appointment_id, ap.animal_id, ap.employee_id, an.owner_name, an.phone, an.species, ap.a_date, ap.a_time, ap.visit_reason, ap.a_status from animals an, appointments ap where an.animal_id = ap.animal_id;"
        data = mysql_handler.fetch_data(query)

        for row in data:
            appointment = Appointment(
                animal_id=int(row[1]),
                vet_id=int(row[2]),
                owner_name=row[3],
                phone_number=row[4],
                species=row[5],
                appointment_date=row[6],
                appointment_time=row[7],
                visit_reason=row[8],
                appointment_status=row[9]
            )
            appointment.appointment_id = int(row[0])
            Appointments.append(appointment)
        mysql_handler.disconnect()
        print(f"Appointments fetched!")
        
    except Exception as err:
        print(f"Appointment Fetch Failed!:{err}") 

def add_appointment(
    animal_id: int,
    vet_id: int,
    owner_name: str,
    phone_number: str,
    species: str,
    appointment_date: str,
    appointment_time: str,
    visit_reason: str,
    appointment_status: str  
):
    try:
        new_appointment = Appointment(
            animal_id,
            vet_id,
            owner_name,
            phone_number,
            species,
            appointment_date,
            appointment_time,
            visit_reason,
            appointment_status
        )
        Appointments.append(new_appointment)

        query = "insert into appointments(animal_id, employee_id, a_date, a_time, visit_reason, a_status) values(%s, %s, %s, %s, %s, %s)"
        values = (animal_id, 
                    vet_id,
                    appointment_date, 
                    appointment_time, 
                    visit_reason, 
                    appointment_status
                    )
        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        mysql_handler.execute_query(query, values)
        
        query = "select count(*) from appointments;"
        appointment_id = int(mysql_handler.fetch_data(query)[0][0])
        mysql_handler.disconnect()
        print("Entry Success!")
        return appointment_id
    except Exception as err:
        print(f"Entry Failed!:{err}") 

def delete_appointment(id:int):
    try:
        for appointment in Appointments: 
            if id == appointment.appointment_id:
                mysql_handler = MySQLHandler()
                mysql_handler.connect()
                query = "delete from appointments where id = %s;"
                data = appointment.appointment.id
                mysql_handler.execute_query(query, (data,))
                Appointments.remove(appointment)
                mysql_handler.disconnect()
                print("Delete Success!")
                break
    except Exception as err:
        print(f"Error: {err}")

def update_appointment(animal_id: int,
    vet_id: int,
    a_date: str,
    a_time: str,
    visit_reason: str,
    a_status: str,
    a_id):
    try:
        mysql_handler = MySQLHandler()
        mysql_handler.connect()

        query = '''
                update appointments set animal_id=%s, employee_id=%s, a_date=%s, a_time=%s, visit_reason=%s, a_status=%s
                where appointment_id = %s;
                '''
        values = (animal_id, vet_id, a_date, a_time, visit_reason, a_status, a_id)
        mysql_handler.execute_query(query, values)
        mysql_handler.disconnect()
        print("Appointment Updated!")
    except Exception as err:
        print(f"Error Updating Appointment: {err}")

def update_appointment_status(apt_id, apt_status):
    try:
        mysql_handler = MySQLHandler()
        mysql_handler.connect()

        query = '''
                update appointments set a_status= %s where appointment_id = %s;
                '''
        values = (apt_status, apt_id)
        mysql_handler.execute_query(query, values)
        mysql_handler.disconnect()
        print("Appointment Cancelled!")
    except Exception as err:
        print(f"Error Cancelling Appointment: {err}")