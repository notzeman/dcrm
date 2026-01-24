import mysql.connector

databse = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
)

print(databse)

cursorObject = databse.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("Database created successfully")
