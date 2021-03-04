def ctr(valeur):
    while valeur<1:
        valeur=input("donner un entier positif")
    return valeur

def parite(x):
    if x%2==0:
        print("paire")
    else:
        print("impaire")
