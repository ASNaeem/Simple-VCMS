import mysql.connector
connection
cursor
def connect():   
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root"
   
    )
    cursor = connection.cursor()
    cursor.execute("use vcms")

def close():
    cursor.close()
    connection.close()