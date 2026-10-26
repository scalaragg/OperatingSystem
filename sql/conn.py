import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="academy",
)
cursor = connection.cursor()

cursor.execute("select * from teachers")

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()