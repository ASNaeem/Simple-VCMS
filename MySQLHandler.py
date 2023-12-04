import mysql.connector


class MySQLHandler:
    def __init__(
        self, host="localhost", user="root", password="root", port=3306, database="vcms"
    ):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.port = port

    def connect(self):
        try:
            print(
                f"Connecting to MySQL database with parameters: {self.host}, {self.user}, {self.database}, {self.port}"
            )
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port,
                autocommit=True
            )
            print("Connected to MySQL database!")
        except mysql.connector.Error as err:
            print(f"Error connecting to MySQL database: {err}")

    def disconnect(self):
        if self.connection:
            try:
                self.connection.close()
                print("Disconnected from MySQL database")
            except Exception as err:
                print(f"Failed to disconnect from MYSQL database: {err}")

    def execute_query(self, query, values=None):
        cursor = self.connection.cursor()
        try:
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
            print("Query executed successfully!")
        except Exception as err:
            print(f"Error connecting to MySQL database: {err}")

            # self.connection.rollback()
        finally:
            cursor.close()

    def fetch_data(self, query, values=None):
        cursor = self.connection.cursor()
        try:
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
            return data
        except Exception as err:
            print(f"Error fetching data: {err}")
