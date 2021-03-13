from controls import *
from rdv import *
date=""
lieu=""
description=""
duree=0
organisation=""
while(date==""):
    date=input("entrer une date : ")
while(lieu==""):
    lieu=input("donner la lieu: ")
while(description==""):
    description=input("decrire letat: ")
while(duree==0):
    duree=int(input("entrer la duree: "))
while(organisation==""):
    organisation=input("donner lorganisation: ")
rd=rdv(date,lieu,description,duree,organisation)
rd.save()
