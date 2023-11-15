class AnimalOwner(Person):
    def __init__ (self, self, name:str, phone:str, email:str, address:str, owner_id:str):
        super().__init__(name, phone, email, address)
        self.owner_id = owner_id

    @property
    def owner_id(self):
        return self._owner_id
    
    @owner_id.setter
    def owner_id(self, owner_id:str):
        self._owner_id = owner_id