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
def pgcd(x,y):
    a=x
    b=y

    while(a!=b):
        if a>b:
            a=a-b
        else:
            b=b-a
    print("le pgcd est %s"%(a))
    return(a)
def ppcm(x,y):
    ppc=((x*y) / (pgcd(x,y)))
    print("le ppcm est %s"%(ppc))

x=0
y=0
valeur=0
x=ctr(x)
parite(x)
y=ctr(y)
fact(y)
pgcd(x,y)
ppcm(x,y)
