from datetime import date
class Animal:
    def __init__ (self, animal_name:str, birth_date:str, 
                    sterilized:str, gender:str, species:str, breed:str, 
                    color:str, behavioral_warning:str, 
                    owner_name:str, email:str, phone:str, address:str, reg_date:str, med_condition:str = None):
        self.animal_id:int = None
        self.animal_name = animal_name
        self.reg_date = reg_date
        self.birth_date = birth_date
        self.sterilized = sterilized
        self.gender = gender
        self.species = species
        self.breed = breed
        self.color = color
        self.med_condition = med_condition
        self.behavioral_warning = behavioral_warning
        self.owner_name = owner_name
        self.email = email
        self.phone = phone
        self.address = address
        self.medical_records = []

    def __str__(self):
        return f"{self.animal.name}"
    def add_record(self, record_id:int, record:str, report_date:str = None):
        if record.strip():
            if not report_date:
                report_date = date.today()
            data = {"record_id":record_id,"record":record, "date":report_date,}
            data = {"record_id":"1","date":"some","record":"rec"}
            self.medical_records.append(data)
        else:
            raise ValueError("Record field can not be empty!")

    
    ### getter, setter ########### 
    @property
    def medical_records(self):
        return self.medical_records
    
    @medical_records.setter
    def medical_records(self, medical_records):
        if all(isinstance(item, dict) and "record_id" in item and "record" in item and "date" in item for item in medical_records):
            self._medical_records = medical_records
        else:
            raise ValueError("Input must be a list of dictionaries with a date and record keys!")
    
    @property
    def animal_id(self):
        return self._animal_id
    
   
    @animal_id.setter
    def animal_id(self, animal_id:int):
        self._animal_id = animal_id
 
    @property
    def animal_name(self):
        return self._animal_name
    @animal_name.setter
    def animal_name(self, animal_name:str):
        self._animal_name = animal_name

    @property
    def birth_date(self):
        return self._birth_date
    @birth_date.setter
    def birth_date(self, birth_date:str):
        self._birth_date = birth_date

    @property
    def breed(self):
        return self._breed
    @breed.setter
    def breed(self, breed: str):
        self._breed = breed
   
    @property
    def species(self):
        return self._species
    @species.setter
    def species(self, species: str):
        self._species = species
   
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color: str):
        self._color = color
   
    @property
    def gender(self):
        return self._gender
    @gender.setter
    def gender(self, gender: str):
        self._gender = gender

    @property
    def reg_date(self):
        return self._reg_date
    @reg_date.setter
    def reg_date(self, reg_date: str):
        self._reg_date = reg_date
   
    @property
    def sterilized(self):
        return self._sterilized
    @sterilized.setter
    def sterilized(self, sterilized: bool):
        self._sterilized = sterilized
   
    @property
    def behavioral_warning(self):
        return self._behavioral_warning
    @behavioral_warning.setter
    def behavioral_warning(self, behavioral_warning: str):
        self._behavioral_warning = behavioral_warning
    
    @property
    def med_condition(self):
        return self._med_condition
    @med_condition.setter
    def med_condition(self, med_condition: str):
        self._med_condition = med_condition

    @property
    def owner_name(self):
        return self._owner_name
    @owner_name.setter
    def owner_name(self, owner_name: str):
        self._owner_name = owner_name

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email: str):
        self._email = email

    @property
    def phone(self):
        return self._phone
    @phone.setter
    def phone(self, phone: str):
        self._phone = phone

    @property
    def address(self):
        return self._address
    @address.setter
    def address(self, address: str):
        self._address = address