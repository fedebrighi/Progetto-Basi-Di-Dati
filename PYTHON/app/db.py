import mysql.connector
from mysql.connector import Error
from app.config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            passwd=DB_PASSWORD,
            database=DB_NAME
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
        else:
            print("Connection to MySQL DB failed")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query, values=None):
    cursor = connection.cursor()
    try:
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def fetch_query(connection, query, values=None):
    cursor = connection.cursor()
    result = None
    try:
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        if result:
            print(f"Fetched {len(result)} rows")
        else:
            print("No rows fetched")
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
