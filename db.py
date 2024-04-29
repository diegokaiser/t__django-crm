import mysql.connector

database = mysql.connector.connect(
    host="django-database.cviii0eoo6dy.eu-north-1.rds.amazonaws.com",
    user="lobogris",
    passwd="$(pB5c&57596-6T"
)

# prepare a cursor object
cursorObject = database.cursor()

# create a database
cursorObject.execute("CREATE DATABASE t__mymproject")

print("Database created successfully")
