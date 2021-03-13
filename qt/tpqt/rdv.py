from controls import *
import mysql.connector
#pip install mysql-connector
mydb = mysql.connector.connect(
host="localhost",
user="root", #username par defaut
passwd="", #password par defaut
database="gestionrdv"
)
#block de départ avant la classe

class rdv:
    #bloc de constructeur== BD
    def __init__(self,date,lieu,description,duree,organisation):
        self.date=date
        self.lieu=lieu
        self.description=description 
        self.duree=duree
        self.organisation=organisation


    def save(self):
        mycursor = mydb.cursor()
        sql = "INSERT INTO `rdv`( `date`, `lieu`, `description`, `duree`, `organisateur`) VALUES  (%s, %s,%s,%s,%s)"
        val = (self.date,self.lieu,self.description,self.duree,self.organisation)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

rd=rdv("25/11/2021","gabes","aucun",30,"personel")
rd.save()
