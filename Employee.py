class Employee:
    def __init__(self, name:str, phone:str, email:str, password:str, address:str, employee_id:int, access_level:int, working_hours:str, designation:str):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        self.address = address
        self.employee_id = employee_id
        self.access_level = access_level
        self.working_hours = working_hours
        self.designation = designation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        self._phone = phone

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password: str):
        self._password = password

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address: str):
        self._address = address
        
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id: int):
        self._employee_id = employee_id

    @property
    def access_level(self):
        return self._access_level
    
    @access_level.setter
    def access_level(self, access_level:int):
        self._access_level = access_level

    @property
    def working_hours(self):
        return self._working_hours
    
    @working_hours.setter
    def working_hours(self, working_hours:str):
        self._working_hours = working_hours

    @property
    def designation(self):
        return self._designation

    @designation.setter
    def designation(self, designation:str):
        self._designation = designation