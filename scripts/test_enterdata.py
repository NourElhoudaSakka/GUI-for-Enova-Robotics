import mysql.connector

db = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "EnovaRobotics123", port = 3306, database = "test")

cursor = db.cursor()

sql = ("INSERT INTO table_de_test VALUES (%s,%s)")
val = ('c','d')
cursor.execute(sql , val)
#cursor.execute("CREATE TABLE table_de_test(test1 VARCHAR(5), test2 VARCHAR(5))")
db.commit()