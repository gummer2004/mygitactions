# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="cr2800"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

#Get User Input
print("Enter a first name:")
name = input()
print ("Select f_name,l_name FROM students where f_name='" + name + "'")
#Retrieve Data
cur.execute(
    "Select f_name,l_name FROM students where f_name='" + name + "'"
)

for (f_name,l_name) in cur:
    print(f"First Name: {f_name}, Last Name: {l_name}")