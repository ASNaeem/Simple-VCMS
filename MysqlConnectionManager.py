import mysql.connector
def establish_connection():   
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root"
    )
    cursor = mydb.cursor()
    cursor.execute("use vcms")
