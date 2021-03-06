#classe principale
import mysql.connector

class produit:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root", #username par defaut
    passwd="", #password par defaut
    database="sante"
    )
    def __init__(self,titre,prixu,prixv,quantite):
        self.titre=titre
        self.prixu=prixu
        self.prixv=prixv
        self.quantite=quantite
    def gain_brute(self):
        gain=(self.prixv-self.prixu)*self.quantite
        return gain
    def taxe(self):
        if(self.prixv<100):
            return self.prixv*0.04
        elif(self.prixv<500):
            return self.prixv*0.09
        else:
            return self.prixv*0.12
    def read(self):
        while(self.titre==""):
            self.titre=input("titre=? ")
        while(self.prixu<1):
            self.prixu=float(input("donner votre prix d'achat"))
        while(self.prixv<1 or self.prixv<self.prixu):
            self.prixv=float(input("donner le prix de vente"))
        while(self.quantite<1):
            self.quantite=int(input("donner la quantité"))
    def detailles(self):
        print("le produit est: %s le prix d'achat est de: %s le prix de vente est %s avec une quantité de stock de: %s"%(self.titre,self.prixu,self.prixv,self.quantite))
    def add(self):
        mycursor = mydb.cursor() #placer le curseur en pointant sur la DB
        sql = "INSERT INTO `personne`( `nom`, `age`, `etat`) VALUES (%s, %s,%s)"
        val = (nom,age, etat)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")



#programme de test
"""
pr1=produit("MSI gamer",3700,4100,2)
chiffre=pr1.gain_brute()
print("votre chiffre de gain estimé est de : %s"%(chiffre))
taxes=pr1.taxe()
print("la taxe unitaire à payer est de %s"%(taxes))
"""

