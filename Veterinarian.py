class Veterinarian(Employee):
    def __init__ (self, name:str, phone:str, email:str, address:str, password:str, access_level:int, working_hours:str, designation:str, total_cases:int, specialization:str):
        super().__init__(name, phone, email, address, password, access_level, working_hours, designation)
        self.total_cases = total_cases
        self.specialization = specialization
        
    ### getter, setter########### 
    @property
    def total_cases(self):
        return self._total_cases
    @total_cases.setter
    def total_cases(self, total_cases:int):
        self._total_cases = total_cases

    @property
    def specialization(self):
        return self._specialization
    @specialization.setter
    def specialization(self, specialization:str):
        self._specialization = specialization
    
    