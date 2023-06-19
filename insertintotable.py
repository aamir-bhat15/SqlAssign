import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("insert into TEST2.TEST2_TABLE values(25,'Aamir')")
mydb.commit()
mydb.close()