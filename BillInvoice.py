class BillInvoice:
    def __init__(self, billing_id:str, animal_id:str, total_amount:float):
        self.billing_id = billing_id
        self.animal_id = animal_id
        self.total_amount = total_amount
    
    @property
    def billing_id(self):
        return self._billing_id

    @billing_id.setter
    def billing_id(self, billing_id:str):
        self._billing_id = billing_id

    @property
    def animal_id(self):
        return self._animal_id

    @animal_id.setter
    def animal_id(self, animal_id:str):
        self._animal_id = animal_id

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount:str):
        self._total_amount = total_amount