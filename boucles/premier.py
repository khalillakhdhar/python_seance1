x=int(input("donner un entier "))
i=2
while x %i !=0 and i< (x/2):
    i+=1
if i>(x/2):
    print("premier")
else:
    print("n'est pas premier")