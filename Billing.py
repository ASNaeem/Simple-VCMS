import Operations as op
from datetime import date

#service_id_input = input()

class Bill:
    def __init__(self, 
                day_care_id:int, 
                appointment_id:int, 
                payment_date:str, 
                total_amount:float, 
                adjustment:float,
                services:int = None,
                status:str = "Due"):
        self.billing_id = None
        self.day_care_id = day_care_id
        self.appointment_id = appointment_id
        self.payment_date = payment_date
        self.total_amount = total_amount
        self.adjustment = adjustment
        self.status = status
        self.services = []
    
    ########getter, setter###########
    def add_services(self, service_id_input:int):
        self.services.append(service_id)
        ...
    
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
    def adjustment(self):
        return self._adjustment
    @adjustment.setter
    def adjustment(self, adjustment:float):
        self._adjustment = adjustment

    @property
    def payment_date(self):
        return self._payment_date
    @payment_date.setter
    def payment_date(self, payment_date:str):
        self._payment_date = payment_date

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, status:str):
        self._status = status