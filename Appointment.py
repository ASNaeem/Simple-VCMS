class Appointment:
    def __init__(
        self,
        animal_id: int,
        appointment_date: str,
        appointment_time: str,
        visit_reason: str,
        appointment_status: str,
    ):
        self.appointment_id = None
        self.animal_id = animal_id
        self.owner_name = owner_name
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.visit_reason = visit_reason
        self.appointment_status = appointment_status

    ########getter, setter###########
    @property
    def appointment_id(self):
        return self._appointment_id

    """
    @appointment_id.setter
    def appointment_id(self, appointment_id: int):
        self._appointment_id = appointment_id
    """

    @property
    def animal_id(self):
        return self.animal_id

    @animal_id.setter
    def animal_id(self, animal_id: int):
        self._animal_id = animal_id

    @property
    def appointment_date(self):
        return self._appointment_date

    @appointment_date.setter
    def appointment_date(self, appointment_date: str):
        self._appointment_date = appointment_date

    @property
    def appointment_time(self):
        return self._appointment_time

    @appointment_time.setter
    def appointment_time(self, appointment_time: str):
        self._appointment_time = appointment_time

    @property
    def visit_reason(self):
        return self._visit_reason

    @visit_reason.setter
    def visit_reason(self, visit_reason: str):
        self._visit_reason = visit_reason

    @property
    def appointment_status(self):
        return self._appointment_status

    @appointment_status.setter
    def appointment_status(self, appointment_status: str):
        self._appointment_status = appointment_status
    ########getter, setter end###########

###  Appointment #####
def add_appointment(
    date,
    time,
    reason: str,
    name: str,
    phone: str,
    address: str,
    animal_name: str,
    species: str,
    breed: str,
    color: str,
    behaviour: str,
    birth: str,
    reg_date: str,
):
    apt = Appointment(date, time, re)