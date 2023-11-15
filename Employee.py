class Employee(Person):
    def __init__ (self, name:str, phone:str, email:str, address:str, employee_id:str, user_name:str, password:str, access_level:int, working_hours:str):
        super().__init__(name, phone, email, address)
        self.employee_id = employee_id
        self.user_name = user_name
        self.password = password
        self.access_level = access_level
        self.working_hours = working_hours
    
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id: str):
        self._employee_id = employee_id

    @property
    def user_name(self):
        return self._user_name
    
    @user_name.setter
    def user_name(self, user_name:str):
        self._user_name = user_name
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password:str):
        self._password = password

    @property
    def access_level(self):
        return self._access_level
    
    @access_level.setter
    def access_level(self, access_level:str):
        self._access_level = access_level

    @property
    def working_hours(self):
        return self._working_hours
    
    @working_hours.setter
    def working_hours(self, working_hours:str):
        self._working_hours = working_hours
