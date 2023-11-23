class Animal:
    def __init__ (self, animal_id:str, breed:str, species:str, color:str, gender:str, age:str, registration_date:str, sterillized:bool, behavioral_warning:str, medical_condition:str):
         self.animal_id = animal_id
         self.breed = breed
         self.species = species
         self.color = color
         self.gender = gender
         self.age = age
         self.registration_date = registration_date
         self.sterillized = sterillized
         self.behavioral_warning = behavioral_warning 
         self.medical_condition = medical_condition
    @property
    def animal_id(self):
        return self._animal_id
    @animal_id.setter
    def animal_id(self, animal_id: str):
        self._animal_id = animal_id
    
    @property
    def breed(self):
        return self._breed
    @breed.setter
    def breed(self, breed: str):
        self._breed_ = breed
   
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
    def age(self):
        return self._age
    @age.setter
    def age(self, age: str):
        self._age = age
    
    @property
    def registration_date(self):
        return self._registration_date
    @registration_date.setter
    def registration_date(self, registration_date: str):
        self._registration_date = registration_date
   
    @property
    def sterillized(self):
        return self._sterillized
    @sterillized.setter
    def sterillized(self, sterillized: bool):
        self._sterillized = sterillized
   
    @property
    def behavioral_warning(self):
        return self._behavioral_warning
    def behavioral_warning(self, behavioral_warning: str):
        self._behavioral_warning = behavioral_warning
    
    @property
    def medical_condition(self):
        return self._medical_condition
    @medical_condition.setter
    def medical_condition(self, medical_condition: str):
        self._medical_condition = medical_condition
