import mysql.connector
#pip install mysql-connector
mydb = mysql.connector.connect(
host="localhost",
user="root", #username par defaut
passwd="", #password par defaut
database="sante"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT nom,age FROM personne WHERE age >25")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)