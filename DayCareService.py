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
    animal_id: int,
    day_care_date: str,
    start_time: str,
    end_time: str,
    notes: str,
):
    try:
        new_day_care = DayCareService(
            animal_id, day_care_date, start_time, end_time, notes
        )
        Day_Care_Service.append(new_day_care)

        query = "insert into day_care (animal_id, dos, start_time, end_time, notes) values (%S, %s, %s, %s, %s);"
        data = values(animal_id, day_care_date, start_time, end_time, notes)

        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        mysql_handler.execute_query(query, data)
        mysql_handler.disconnect()
        print("Entry Success!")
    except Exception as err:
        print(f"Entry Failed: {err}")


def delete_day_care(id: int):
    try:
        for day_care in Day_Care_Service:
            if id == day_care.id:
                mysql_handler = MySQLHandler()
                mysql_handler.connect()
                query = "delete from day_care where day_care_id = %s;"
                data = day_care.id
                mysql_handler.execute_query(query, data)
                Day_Care_Service.remove(day_care)
                mysql_handler.disconnect()
                print("Delete Success!")
        print("Delete Failed!")
    except Exception as err:
        print(f"Error: {err}")


##################### Day Care Operations End #########################
