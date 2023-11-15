class BillInvoice:
    def __init__(self, billing_id:str, patient_id:str, total_amount:float):
        self.billing_id = billing_id
        self.patient_id = patient_id
        self.total_amount = total_amount
    
    @property
    def billing_id(self):
        return self._billing_id

    @billing_id.setter
    def billing_id(self, billing_id:str):
        self._billing_id = billing_id

    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, patient_id:str):
        self._patient_id = patient_id

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount:str):
        self._total_amount = total_amount