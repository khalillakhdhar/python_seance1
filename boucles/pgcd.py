a=18
b=4
x=a
y=b
while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
print(" le pgcd de %s et %s est: %s"%(x,y,a))