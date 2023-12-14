from MySQLHandler import MySQLHandler


class Employee:
    def __init__(
        self,
        name: str,
        email: str,
        password: str,
        address: str,
        designation: str,
        access_level: int,
        # working_hours: str,
        salary: float,
        joining_date: str,
        employee_status: str,
        phone: str = [],
    ):
        self.employee_id = None
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.designation = designation
        self.access_level = access_level
        # self.working_hours = working_hours
        self.salary = salary
        self.joining_date = joining_date
        self.employee_status = employee_status
        self.phone = phone

    ########getter, setter###########
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id: int):
        self._employee_id = employee_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone: str = []):
        self._phone = phone

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password: str):
        self._password = password

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address: str):
        self._address = address

    @property
    def access_level(self):
        return self._access_level

    @access_level.setter
    def access_level(self, access_level: int):
        self._access_level = access_level

    """@property
    def working_hours(self):
        return self._working_hours

    @working_hours.setter
    def working_hours(self, working_hours: str):
        self._working_hours = working_hours"""

    @property
    def designation(self):
        return self._designation

    @designation.setter
    def designation(self, designation: str):
        self._designation = designation

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary: float):
        self._salary = salary

    @property
    def joining_date(self):
        return self._joining_date

    @joining_date.setter
    def joining_date(self, joining_date: str):
        self._joining_date = joining_date

    @property
    def employee_status(self):
        return self._employee_status

    @employee_status.setter
    def employee_status(self, employee_status: str):
        self._employee_status = employee_status

    ########getter, setter end###########


##################### Employee Operations #########################

Employees = []

def fetch_employees():
    Employees.clear()
    try:
        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        query = "select * from employees"
        data = mysql_handler.fetch_data(query)
        for row in data:
            query = "select phone from phones where employee_id = %s"
            value = row[0]
            phone_data = mysql_handler.fetch_data(query, (value,))
            phone_numbers = [phone[0] for phone in phone_data]
            employee = Employee(
                name=row[1],
                email=row[2],
                password=row[3],
                address=row[4],
                designation=row[5],
                access_level=row[6],
                salary=row[7],
                joining_date=row[8],
                employee_status=row[9],
                phone=phone_numbers,
            )
            print(employee.phone)
            employee.employee_id = int(row[0])
            Employees.append(employee)
        mysql_handler.disconnect()
    except Exception as err:
        print(f"Error Fetching: {err}")


def add_employee(
    name: str,
    email: str,
    password: str,
    address: str,
    access_level: int,
    # working_hours: str,
    designation: str,
    salary: float,
    joining_date: str,
    employee_status: str,
    phone=[],
):
    try:
        new_employee = Employees(
            name,
            email,
            password,
            address,
            access_level,
            # working_hours,
            designation,
            salary,
            joining_date,
            employee_status,
            phone,
        )
        Employee.append(new_employee)

        query = "insert into employees (name, email, password, address, designation, access_level, salary, joining_date) values (%s, %s, %s, %s, %s, %s, %s, %s);"
        data = values(
            name,
            email,
            password,
            address,
            designation,
            access_level,
            # working_hours,
            salary,
            joining_date,
            employee_status,
        )

        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        mysql_handler.execute_query(query, data)
        query = "insert into phones (id, phone_number) values(%s, %s);"
        query_fetch_id = "select id from employees order by id desc limit 1;"
        row = mysql_handler.fetch_data(query_fetch_id)
        id = row[0]
        # data = values(row[0][0], phone)
        data1 = values(id, phone[0])
        data2 = values(id, phone[1])
        mysql_handler.execute_query(query, data1)
        mysql_handler.execute_query(query, data2)
        mysql_handler.disconnect()
        print("Entry Success!")
    except Exception as err:
        print("Entry Failed: {err}")


def delete_employee(id: int):
    try:
        for employee in Employees:
            if id == employee.employee_id:
                mysql_handler = MySQLHandler()
                mysql_handler.connect()
                query = "delete from employees where employee_id = %s;"
                data = employee.employee_id
                mysql_handler.execute_query(query, (data,))
                Employees.remove(employee)
                mysql_handler.disconnect()
                print("Delete Success!")
                break
    except Exception as err:
        print(f"Error: {err}")


def update_employee_to_db(employee_id, name, email, password, 
                    address, designation, access_level, 
                    salary, joining_date, employee_status):
    try:
        mysql_handler = MySQLHandler()
        mysql_handler.connect()

        query = '''
                UPDATE employees
                SET
                name = %s,
                email = %s,
                password = %s,
                address = %s,
                designation = %s,
                access_level = %s,
                salary = %s,
                joining_date = %s,
                employee_status = %s
                WHERE
                employee_id = %s
                '''
        values = (name, email, password, 
                address, designation, access_level, 
                salary, joining_date, employee_status, employee_id)

        mysql_handler.execute_query(query, values)
        mysql_handler.disconnect()
        print("Employee Information Updated!")

    except Exception as err:
        print(f"Employee Update Failed!: {err}")

def update_employee_phone_to_db(employee_id:int, phone1, phone1prev, phone2, phone2prev):
    try:
        mysql_handler = MySQLHandler()
        mysql_handler.connect()

        query1 = "UPDATE phones SET phone = %s WHERE employee_id = %s and phone = %s"
        values1 = (phone1, employee_id, phone1prev)
        mysql_handler.execute_query(query1, values1)

        query2 = "UPDATE phones SET phone = %s WHERE employee_id = %s and phone = %s"
        values2 = (phone2, employee_id, phone2prev)
        mysql_handler.execute_query(query2, values2)

        mysql_handler.disconnect()
        print("Employee Phone Numbers Updated!")

    except Exception as err:
        print(f"Employee Phone Number Update Failed!: {err}")

def update_employee_status(emp_id:int, status: str):
    try:
        mysql_handler = MySQLHandler()
        mysql_handler.connect()

        query = "UPDATE employees SET status = %s where employee_id = %s"
        values = (status, emp_id)
        mysql_handler.execute_query(query, values)

        mysql_handler.disconnect()
        print("Employee Resigned!")

    except Exception as err:
        print(f"Employee Status Update Failed!: {err}")


##################### End of Employee #########################
