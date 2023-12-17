import os
import mysql.connector


class MySQLHandler:
    CONFIG_FILE_PATH = "mysql_config.txt"

    def __init__(self, host="localhost", user=None, password=None, port=None, database="vcms"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.port = port

    def load_config_from_file(self):
        if os.path.exists(self.CONFIG_FILE_PATH):
            with open(self.CONFIG_FILE_PATH, "r") as config_file:
                lines = config_file.readlines()
                for line in lines:
                    key, value = map(str.strip, line.split("="))
                    if key == "user":
                        self.user = value
                    elif key == "password":
                        self.password = value
                    elif key == "port":
                        self.port = int(value)

    def save_config_to_file(self):
        with open(self.CONFIG_FILE_PATH, "w") as config_file:
            config_file.write(f"user = {self.user}\n")
            config_file.write(f"password = {self.password}\n")
            config_file.write(f"port = {self.port}\n")

    def connect(self):
        try:
            self.load_config_from_file()

            print(
                f"Connecting to MySQL database with parameters: {self.host}, {self.user}, {self.database}, {self.port}"
            )
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port,
                autocommit=True,
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
