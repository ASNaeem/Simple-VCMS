class Appointment:
    def __init__(
        self,
        appointment_id: int,
        animal_id: int,
        appointment_date: str,
        appointment_time: str,
        visit_reason: str,
        appointment_status: str,
    ):
        self.appointment_id = appointment_id
        self.animal_id = animal_id
        self.owner_name = owner_name
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.visit_reason = visit_reason
        self.appointment_status = appointment_status

    @property
    def appointment_id(self):
        return self._appointment_id

    @appointment_id.setter
    def appointment_id(self, appointment_id: str):
        self._appointment_id = appointment_id

    @property
    def animal_id(self):
        return self.animal_id

    @animal_id.setter
    def animal_id(self, animal_id: str):
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
    def appoinmrnt_status(self):
        return self._appoinmrnt_status

    @appoinmrnt_status.setter
    def appoinmrnt_status(self, appoinmrnt_status: str):
        self._appoinmrnt_status = appoinmrnt_status
