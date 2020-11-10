import mysql.connector
from mysql.connector import Error

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created succesfully")
    except Error as e:
        print(f"The error '{e}' occured")