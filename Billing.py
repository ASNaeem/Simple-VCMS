from datetime import date
from MySQLHandler import MySQLHandler


class Bill:
    def __init__(
        self,
        day_care_id: int,
        appointment_id: int,
        billing_date: str,
        total_amount: float,
        adjustment: float,
        status: str = "Due",
    ):
        self.billing_id = None
        self.day_care_id = day_care_id
        self.appointment_id = appointment_id
        self.billing_date = billing_date
        self.total_amount = total_amount
        self.adjustment = adjustment
        self.status = status
        self.services = []

    ########getter, setter###########
    def add_services(self, service_id: int):
        self.services.append(service_id)
        ...

    @property
    def billing_id(self):
        return self._billing_id

    @billing_id.setter
    def billing_id(self, billing_id: int):
        self._billing_id = billing_id

    @property
    def day_care_id(self):
        return self._day_care_id

    @day_care_id.setter
    def day_care_id(self, day_care_id: int):
        self._day_care_id = day_care_id

    @property
    def appointment_id(self):
        return self._appointment_id

    @appointment_id.setter
    def appointment_id(self, appointment_id: int):
        self._appointment_id = appointment_id

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount: float):
        self._total_amount = total_amount

    @property
    def adjustment(self):
        return self._adjustment

    @adjustment.setter
    def adjustment(self, adjustment: float):
        self._adjustment = adjustment

    @property
    def billing_date(self):
        return self._billing_date

    @billing_date.setter
    def billing_date(self, billing_date: str):
        self._billing_date = billing_date

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status: str):
        self._status = status

    ########getter, setter end###########


### Billing ####
Billings = []


def fetch_billings():
    try:
        Billings.clear()
        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        query = "select * from billings;"
        data = mysql_handler.fetch_data(query)
        query = "select * from bill_services;"
        dataServices = mysql_handler.fetch_data(query)
        day_care_id_previous = None
        for row in data:
            if row[1] == None:
                day_care_id_previous = 0
            else:
                day_care_id_previous = int(row[1])
            billing = Bill(
                day_care_id = day_care_id_previous, 
                appointment_id=int(row[2]),
                billing_date=str(row[3]),
                total_amount=float(row[4]),
                adjustment=float(row[5]),
                status=row[6],
            )
            billing.billing_id = int(row[0])
            for rowServices in dataServices:
                if billing.billing_id == rowServices[0]:
                    billing.add_services(rowServices[1])

            Billings.append(billing)
        mysql_handler.disconnect()
    except Exception as err:
        print(f"Error Fetching(fetch_billings): {err}")


def add_bill(
    day_care_id: int,
    appointment_id: int,
    billing_date: str,
    total_amount: float,
    adjustment: float,
    status: str,
):
    try:
        billing_date = date.today()
        new_bill = Bill(
            day_Care_id, appointment_id, currentDate, total_amount, adjustment, status
        )
        Billings.append(new_bill)

        query = "insert into animal (day_care_id, appointment_id, billing_date, total_amount, adjustment, status) values(%s,%s,%s,%s,%s,%s)"
        values = (
            day_care_id,
            appointment_id,
            billing_date,
            total_amount,
            adjustment,
            status,
        )
        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        mysql_handler.execute_query(query, values)
        print("Entry Success!")
        mysql_handler.disconnect()
        print("Entry Success!")
    except Exception as err:
        print(f"Error: {err}")


def delete_bill(id: int):
    try:
        for billing in Billings:
            if id == billing.billing_id:
                mysql_handler = MySQLHandler()
                mysql_handler.connect()
                query = "delete from Billings where biid = %s;"
                data = id
                mysql_handler.execute_query(query, (data,))
                Billings.remove(billing)
                mysql_handler.disconnect()
                print("Delete Success!")
            else:
                print("Delete Failed!")
    except Exception as err:
        print(f"Error(delete_bill): {err}")

def update_bill(total_amount, adjustment, status, bill_id):
    try:
        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        query = "update billings set total_amount = %s, adjustment = %s, status = %s where bid = %s;"
        values = (total_amount, adjustment, status, bill_id)
        mysql_handler.execute_query(query, values)
        mysql_handler.disconnect()
        print("Bill Updated")
    except Exception as err:
        print(f"Error Fetching(update_bill_billing_class): {err}")
### End Billing ####
