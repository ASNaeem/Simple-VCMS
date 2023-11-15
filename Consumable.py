class Consumable(Inventory):
    def __init__(self, item_name:str, item_manufacture:str, item_price:float, stock: int):
        super().__init__(item_name, item_manufacture, item_price)
        self.stock = stock

    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, stock:int):
        self._stock = stock

    def pop(amount = 1):
        self.stock -= amount

    def push(amount = 1):
        self.stock += amount