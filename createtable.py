import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE TEST2.TEST2_TABLE(Age int, Name varchar(50))")
mydb.close()
