import mysql.connector

# Replace with your own database credentials
config = {
    'user': 'root',
    'password': 'yes@2871',
    'host': 'localhost',
    'database': 'Mann'
}

try:
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        print("Successfully connected to the database")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if connection.is_connected():
        connection.close()
        print("Connection closed")
