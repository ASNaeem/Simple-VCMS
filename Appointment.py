import datetime
class Appointment :
    def __init__ (self, appointment_id:str, appointment_date: date, appointment_time:str, owner_name:str,owner_phone:str, animal_name:str, animal_species:str, visit_reason:str, veterinarian_name:str, appoinmrnt_status:str) :
        self.appointment_id = appointment_id
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.owner_name = owner_name
        self.owner_phone = owner_phone
        self.animal_name = animal_name
        self.animal_species = animal_species
        self.visit_reason = visit_reason
        self.veterinarian_name = veterinarian_name
        self.appoinmrnt_status = appoinmrnt_status
   
    @property
    def appointment_id(self):
        return self._appointment_id
    
    @appointment_id.setter
    def appointment_id(self, appointment_id: str):
        self._appointment_id = appointment_id
    
    @property
    def appointment_date (self):
        return self._appointment_date
   
    @appointment_date.setter
    def appointment_date (self, appointment_date:date ):
        self._appointment_date = appointment_date
   
    @property
    def appointment_time(self):
        return self._appointment_time
    
    @appointment_time.setter
    def appointment_time(self, appointment_time: str):
        self._appointment_time = appointment_time
    
    @property
    def owner_name(self):
        return self._owner_name
    
    @owner_name.setter
    def appointment_time(self, owner_name: str):
        self._owner_name = owner_name
    
    @property
    def owner_phone(self):
        return self._owner_phone
    
    @owner_phone.setter
    def owner_phone(self, owner_phone: str):
        self._owner_phone = owner_phone
    
    @property
    def animal_name(self):
        return self._animal_name
    
    @animal_name.setter
    def animal_name(self, animal_name: str):
        self._animal_name = animal_name
    
    @property
    def animal_species(self):
        return self._animal_species
    
    @animal_species.setter
    def animal_species(self, animal_species: str):
        self._animal_species = animal_species
   
    @property
    def visit_reason(self):
        return self._visit_reason
    
    @visit_reason.setter
    def visit_reason(self, visit_reason: str):
        self._visit_reason = visit_reason
    
    @property
    def veterinarian_name(self):
        return self._veterinarian_name
    
    @veterinarian_name.setter
    def veterinarian_name(self, veterinarian_name: str):
        self._veterinarian_name = veterinarian_name

    @property
    def appoinmrnt_status(self):
        return self._appoinmrnt_status
    
    @appoinmrnt_status.setter
    def appoinmrnt_status(self, appoinmrnt_status: str):
        self._appoinmrnt_status = appoinmrnt_status