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
        if(self.prixv<100):
            return self.prixv*0.04
        elif(self.prixv<500):
            return self.prixv*0.09
        else:
            return self.prixv*0.12


#programme de test
"""
pr1=produit("MSI gamer",3700,4100,2)
chiffre=pr1.gain_brute()
print("votre chiffre de gain estimé est de : %s"%(chiffre))
taxes=pr1.taxe()
print("la taxe unitaire à payer est de %s"%(taxes))
"""