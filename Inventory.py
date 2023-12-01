class Inventory:
    def __init__(self, manager_id:int, name:str, 
                manufacturer:str, item_type:str, price:float, amount:int):
        self.item_id = None
        self.name = name
        self.manager_id = manager_id
        self.manufacturer = manufacturer
        self.price = price
        self.item_type = item_type
        self.amount = amount

###Getter, Setter###
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name:str):
        self._name = name
    
    @property
    def item_id(self):
        return self._item_id
    '''
    @item_id.setter
    def item_id(self, item_id:int):
        self._item_id = item_id
    '''

    @property
    def manager_id(self):
        return self._manager_id
    @manager_id.setter
    def manager_id(self, manager_id:int):
        self._manager_id = manager_id

    @property
    def item_type(self):
        return self._item_type
    @item_type.setter
    def item_type(self, item_type:str):
        self._item_type = item_type


    @property
    def manufacturer(self):
        return self._manufacturer
    @manufacturer.setter
    def manufacturer(self, manufacturer:str):
        self._manufacturer = manufacturer

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price:float):
        self._price = price

    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self, amount:int):
        self._amount = amount