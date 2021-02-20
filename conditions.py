brute=1800.0
taxe=0
if brute < 700:
    taxe=0
elif brute<1500:
    taxe=float(brute*0.15)
else:
    taxe=float(brute*0.19)
nette=brute-taxe
print("votre salaire est de %s la taxe à payer est %s et le nette à obtenir est de: %s"%(brute,taxe,nette))