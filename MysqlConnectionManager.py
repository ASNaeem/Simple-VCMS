import mysql.connector
connection
cursor
def connect(): 
    try:  
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root"
    
        )
        cursor = connection.cursor()
        cursor.execute("use vcms")
    except Exception as err:
        print(f"Error: {err}")

def close():
    try:
        cursor.close()
        connection.close()
    except Exception as err:
        print(f"Error: {err}")