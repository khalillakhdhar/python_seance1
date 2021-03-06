#classe principale
class produit:
    def __init__(self,titre,prixu,prixv,quantite):
        self.titre=titre
        self.prixu=prixu
        self.prixv=prixv
        self.quantite=quantite
    def gain_brute(self):
        gain=(self.prixv-self.prixu)*self.quantite
        return gain
    def taxe(self):
        

#programme de test
pr1=produit("MSI gamer",3700,4100,2)
chiffre=pr1.gain_brute()
print("votre chiffre de gain estimé est de : %s"%(chiffre))