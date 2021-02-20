#x=int(input("donner un entier à 3 chiffre "))
x=980
c=x//100
#print(c)
d=(x%100)//10
#print(d)
u=x%10
s=c+d+u
print("la somme des chiffres de %s est %s"%(x,s) )