from datetime import date
from MySQLHandler import MySQLHandler


class DayCareService:
    def __init__(
        self,
        animal_id: int,
        day_care_date: str,
        start_time: str,
        end_time: str,
        notes: str,
    ):
        self.day_Care_id = None
        self.animal_id = animal_id
        self.day_care_date = day_care_date
        self.start_time = start_time
        self.end_time = end_time
        self.notes = notes

    ######### getter, setter #############
    @property
    def day_Care_id(self):
        return self._day_Care_id

    @day_Care_id.setter
    def day_Care_id(self, day_Care_id: str):
        self._day_Care_id = day_Care_id

    @property
    def animal_id(self):
        return self._animal_id

    @animal_id.setter
    def animal_id(self, animal_id: str):
        self._animal_id = animal_id

    @property
    def day_care_date(self):
        return self._day_care_date

    @day_care_date.setter
    def day_care_date(self, day_care_date: str):
        self._day_care_date = day_care_date

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time: str):
        self._start_time = start_time

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, end_time: str):
        self._end_time = end_time

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, notes: str):
        self._notes = notes

    ######### getter, setter end #############


##################### Day Care Operations #########################

Day_Care_Service = []


def fetch_day_care():
    try:
        Day_Care_Service.clear()
        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        query = "select * from day_care;"
        data = mysql_handler.fetch_data(query)

        for row in data:
            dayCareService = DayCareService(
                animal_id=row[1],
                day_care_date=str(row[2]),
                start_time=str(row[3]),
                end_time=str(row[4]),
                notes=str(row[5]),
            )
            dayCareService.day_Care_id = int(row[0])
            Day_Care_Service.append(dayCareService)
        mysql_handler.disconnect()
    except Exception as err:
        print(f"Error Fetching: {err}")


def add_day_care(
    animal_id,
    day_care_date,
    start_time,
    notes,
    end_time = None
):
    try:
        query = "insert into day_care (animal_id, dos, start_time, notes) values (%s, %s, %s, %s);"
        data = animal_id, day_care_date, start_time, notes

        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        mysql_handler.execute_query(query, data)

        LAST_INSERT_ID = mysql_handler.fetch_data("Select count(*) from day_care")
        new_day_care_id =  LAST_INSERT_ID[0][0]

        query2 = "UPDATE day_care SET end_time = TIME_ADD(start_time = %s + INTERVAL 1 HOUR) WHERE day_care_id=%s"
        data2 = start_time, new_day_care_id
        mysql_handler.execute_query(query2, data2)

        mysql_handler.disconnect()
        print("Entry Success!")
        return new_day_care_id
    except Exception as err:
        print(f"Entry Failed: {err}")


def delete_day_care(id: int):
    try:
        for day_care in Day_Care_Service:
            if id == day_care.day_Care_id:
                mysql_handler = MySQLHandler()
                mysql_handler.connect()
                query = "delete from day_care where day_care_id = %s;"
                data = id
                mysql_handler.execute_query(query, (data,))
                Day_Care_Service.remove(day_care)
                mysql_handler.disconnect()
                print("Delete Success!")
            else:
                print("Delete Failed!")
    except Exception as err:
        print(f"Error Delete: {err}")

def update_daycare_to_db(
    daycare_id: int, day_care_date_obj: str, start_time: str, end_time: str, notes: str
):
    try:
        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        query = "UPDATE day_care set dos = %s, start_time = %s, end_time = %s, notes = %s where day_care_id = %s;"
        values = (day_care_date_obj, start_time, end_time, notes, daycare_id)

        mysql_handler.execute_query(query, values)
        mysql_handler.disconnect()
        print("Daycare Information Updated!")
    except Exception as err:
        print(f"Daycare Update Failed: {err}")
