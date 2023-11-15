class Inventory:
    def __init__(self, item_name:str, item_manufacture:str, item_price:float):
        self.item_name - item_name
        self.item_manufacture = item_manufacture
        self.item_price = item_price

    @property
    def item_name(self):
        return self._item_name
    
    @item_name.setter
    def item_name(self, item_name:str):
        return self._item_name
    
    @property
    def item_manufacture(self):
        return self._item_manufacture
    
    @item_manufacture.setter
    def item_manufacture(self, item_manufacture:str):
        return self._item_manufacture

    @property
    def item_price(self):
        return self._item_price
    
    @item_price.setter
    def item_price(self, item_price:float):
        return self._item_price