class Employee(Person):
    def __init__ (self, name:str, phone:str, email:str, password:str, address:str, employee_id:str, designation:str, access_level:int, working_hours:str):
        super().__init__(name, phone, email, address, employee_id, password, access_level, working_hours)
        self.designation = designation
    
    @property
    def designation(self):
        return self._designation

    @designation.setter
    def designation(self, designation:str):
        self._designation = designation