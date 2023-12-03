from MySQLHandler import MySQLHandler

user = "root"
password = "root"
host = "localhost"
port = 3306
class Service:
    def __init__(
        self, name: str, cost: float, service_details: str, service_availability: bool
    ):
        self.service_id = None
        self.name = name
        self.cost = cost
        self.service_details = service_details
        self.service_availability = service_availability

    ########getter, setter###########
    @property
    def service_id(self):
        return self._service_id
    
    """
    @service_id.setter
    def service_id(self, service_id:int):
        self._service_id = service_id      
    
    """

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def cost(self):
        return self._cost
    @cost.setter
    def cost(self, cost: float):
        self._cost = cost

    @property
    def service_availability(self):
        return self._service_availability
    @service_availability.setter
    def service_availability(self, service_availability: bool):
        self._service_availability = service_availability

    @property
    def service_details(self):
        return self._service_details
    @service_details.setter
    def service_details(self, service_details: str):
        self._service_details = service_details

        ########getter, setter end###########

### Services List For Billing###
Services = []


def fetch_services():
    try:
        mysql_handler = MySQLHandler(host, user, password, port)
        mysql_handler.connect()
        query = "select * from services"
        data = mysql_handler.fetch_data(query)

        for row in data:
            services = Services(
                name=row[1],
                cost=float(row[2]),
                service_details=row[3],
                service_availability=bool(row[4]),
            )
            services.service_id = int(row[0])
            Services.append(services)
        mysql_handler.disconnect()
    except Exception as err:
        print(f"Error Fethcing: {err}")

def add_service(
    name:str,
    cost:float,
    service_details:str,
    service_availability:bool
):
    try:
        new_service = Service(
            name,
            cost,
            service_details,
            service_availability
        )
        Services.append(new_service)

        query = "insert into services (name, cost, service_details, service_availibility) values(%s,%s,%s,%s)"
        values = (
            name,
            cost,
            service_details,
            service_availability
        )
        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        mysql_handler.execute_query(query, values)
        return "Entry Success!"
        mysql_handler.disconnect()
    except Exception as err:
        return "Entry Failed!"

def delete_service(id:int):
    try:
        for service in Services:
            if id == service.id:
                mysql.connect()
                run_query(f"delete from service where id = {service.id}")
                Services.remove(service)
                mysql.close()
                return "Delete Success!"
        return "Delete Failed!"
    except Exception as err:
        print(f"Error: {err}")
### End Services List For Billing###