import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="sante"
)
mycursor = mydb.cursor()
sql = "INSERT INTO user(nom, adresse) VALUES (%s, %s)"
val = ("khalil", " Gabés")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")