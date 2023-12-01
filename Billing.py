class Bill:
    def __init__(self, 
                day_care_id:int, 
                appointment_id:int, 
                payment_date:str, 
                total_amount:float, 
                services:int = none):
        self.billing_id = None
        self.day_care_id = day_care_id
        self.appointment_id = appointment_id
        self.payment_date = payment_date
        self.total_amount = total_amount
        #self.service_id = []
    
    ########getter, setter###########
    @property
    def billing_id(self):
        return self._billing_id

    @property
    def day_care_id(self):
        return self._day_care_id
    @day_care_id.setter
    def day_care_id(self, day_care_id:int):
        self._day_care_id = day_care_id

    @property
    def appointment_id(self):
        return self._appointment_id
    @appointment_id.setter
    def appointment_id(self, appointment_id:int):
        self._appointment_id = appointment_id

    @property
    def total_amount(self):
        return self._total_amount
    @total_amount.setter
    def total_amount(self, total_amount:float):
        self._total_amount = total_amount

    @property
    def payment_date(self):
        return self._payment_date
    @payment_date.setter
    def payment_date(self, payment_date:str):
        self._payment_date = payment_date