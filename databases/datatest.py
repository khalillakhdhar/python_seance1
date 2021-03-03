import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="sante"
)
mycursor = mydb.cursor()
sql = "INSERT INTO `personne`( `nom`, `age`, `etat`) VALUES (%s, %s,%s)"
val = ("khalil",30, "acceptable")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")