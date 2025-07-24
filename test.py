import mysql.connector
from mysql.connector import Error

cnx = mysql.connector.connect(user='root',
                                  password='Soccer12345!',
                                  host='localhost',
                                  database='Movie')

cursor = cnx.cursor()
cursor.execute("show databases;")
results = cursor.fetchall()
for row in results:
    print(row)

cursor.execute("insert into movies (movieName) values ('GWH');")
cnx.commit()