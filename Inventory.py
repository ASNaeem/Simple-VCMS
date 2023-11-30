class Inventory:
    def __init__(self, item_id:int, manager_id:int, name:str, 
                manufacturer:str, type:str, price:float, amount:int):
        self.item_id = item_id
        self.name = name
        self.manager_id = manager_id
        self.manufacturer = manufacturer
        self.price = price
        self.item_type = item_type
        self.amount = amount

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name:str):
        return self._name
    
    @property
    def item_id(self):
        return self._item_id
    @item_id.setter
    def item_id(self, item_id:str):
        return self._item_id

    @property
    def manager_id(self):
        return self._manager_id
    @manager_id.setter
    def manager_id(self, manager_id:str):
        return self._manager_id

    @property
    def item_type(self):
        return self._item_type
    @item_type.setter
    def item_type(self, item_type:str):
        return self._item_type


    @property
    def manufacturer(self):
        return self._manufacturer
    @manufacturer.setter
    def manufacturer(self, manufacturer:str):
        return self._manufacturer

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price:float):
        return self._price

    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self, amount:float):
        return self._amount