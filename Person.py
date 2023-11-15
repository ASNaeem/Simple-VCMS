class Person:
    def __init__(self, name:str, phone:str, email:str, address:str):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
          
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name:str):
        self._name = name
        
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone:str):
        self._phone = phone

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email:str):
        self._email = email

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address:str):
        self._address = address    
        
        
    
