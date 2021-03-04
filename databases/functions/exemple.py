def ctr(valeur):
    while valeur<1:
        valeur=int(input("donner un entier positif"))
    return valeur

def parite(x):
    if x%2==0:
        print("paire")
    else:
        print("impaire")
def fact(y):
    f=1
    for i in range(2,y+1):
        f=f*i
    print("la factoriel de %s est %s"%(y,f))

x=0
y=0
valeur=0
x=ctr(x)
parite(x)
y=ctr(y)
fact(y)
