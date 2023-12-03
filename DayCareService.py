from datetime import date
from MySQLHandler import MySQLHandler

user = "root"
password = "1234"
host = "localhost"
port = 3307

class DayCareService:
    def __init__(self, 
                animal_id:int, 
                day_care_date:str, 
                start_time:str, 
                end_time:str, 
                notes:str):
        self.day_Care_id = None
        self.animal_id = animal_id
        self.day_care_date = day_care_date
        self.start_time = start_time
        self.end_time = end_time
        self.notes = notes

###Getter, Setter###
    @property
    def day_Care_id(self):
        return self._day_Care_id
    '''@day_Care_id.setter
    def day_Care_id(self, day_Care_id: str):
        self._day_Care_id = day_Care_id'''

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
    def day_care_date(self, naday_care_dateme: str):
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

##################### Day Care Operations #########################

Day_Care = []

def fetch_day_care():
    try:
        mysql_handler = MySQLHandler(host, user, password, port)
        mysql_handler.connect()
        query = "select * from day_care;"
        data = mysql_handler.fetch_data(query)
        
        for row in data:
            #day_care = Day_Care
            pass

    except Exception as err:
        pass
