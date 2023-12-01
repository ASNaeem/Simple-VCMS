import mysql.connector
class MySQLHandler:
    def __init__(self, host = "localhost", user="root", password="root", database="vcsm"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        
    def connect(self):
        try:
            self.connection = mysql.connector.connect(host=self.host,user=self.user,
                                                        password=self.password, database = self.database)
            print("Connected to MySQL database!")
        except Exception as err:
            print("Error connecting to MySQL database: {err}")
            
    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from MySQL database")
            
    def execute_query(self, query, values=None):
        try:
            cursor = self.connection.cursor()
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
            print("Query executed successfully!")
        except Exception as err:
            print(f"Error executing query: {err}")
            #self.connection.rollback()
        finally:
            cursor.close()
    def fetch_data(self, query, values=None):
        try:
            cursor = self.connection.cursor()
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
            return data
        except Exception as err:
            print(f"Error fetching data: {err}")    