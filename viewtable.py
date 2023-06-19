import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("select * from TEST2.TEST2_TABLE")
for i in mycursor.fetchall():
    print(i)