class Equipment(Inventory):
    def __init__(self, item_name:str, item_manufacture:str, item_price:float, equipment_id: str, equipment_model: str, equipment_Status: bool):
        super().__init__(item_name, item_manufacture, item_price)
        self.equipment_id = equipment_id
        self.equipment_model = equipment_model
        self.equipment_status = equipment_Status

    @property
    def equipment_id(self):
        return self._equipment_id
    
    @equipment_id.setter
    def equipment_id(self, equipment_id:str):
        self._equipment_id = equipment_id

    @property
    def equipment_model(self):
        return self._equipment_model
    
    @equipment_model.setter
    def equipment_model(self, equipment_model:str):
        self._equipment_model = equipment_model

    @property
    def equipment_status(self):
        return self._equipment_status
    
    @equipment_status.setter
    def equipment_status(self, equipment_status:bool):
        self._equipment_status = equipment_status

    def update_equipment_status(self):
        if self.equipment_status == False:
            self.equipment_status = True
        else:
            self.equipment_status = False