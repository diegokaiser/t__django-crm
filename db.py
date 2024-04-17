import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor"
)

# prepare a cursor object
cursorObject = database.cursor()

# create a database
cursorObject.execute("CREATE DATABASE t__mymproject")

print("Database created successfully")
