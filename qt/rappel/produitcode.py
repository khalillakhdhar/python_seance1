from produitcl import *
rep=int(input("donner le nombre de produits à ajouter" ))
produit1=produit("",0,0,0)
for i in range(rep):
    produit1=produit("",0,0,0)
    produit1.read()
    produit1.add()
    #produit1.detailles()
print("(id, titre, prix achat, prix vente)")
produit1.afficher()