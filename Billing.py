class Bill:
    def __init__(self, billing_id:int, day_care_id:int, appointment_id:int, payment_date:int, total_amount:float):
        self.billing_id = billing_id
        self.day_care_id = day_care_id
        self.appointment_id = appointment_id
        self.payment_date = payment_date
        self.total_amount = total_amount
    
    @property
    def billing_id(self):
        return self._billing_id

    @billing_id.setter
    def billing_id(self, billing_id:str):
        self._billing_id = billing_id

    @property
    def day_care_id(self):
        return self._day_care_id

    @day_care_id.setter
    def day_care_id(self, day_care_id:str):
        self._day_care_id = day_care_id

    @property
    def appointment_id(self):
        return self._appointment_id

    @appointment_id.setter
    def appointment_id(self, appointment_id:str):
        self._appointment_id = appointment_id

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount:str):
        self._total_amount = total_amount