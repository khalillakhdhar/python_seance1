class controls:
    def __init__(self,valeur):
        self.valeur=valeur
    def ctrstring(self):
        if (self.valeur==""):
            return false 
    def ctrnumber(self):
        if(self.valeur<=0):
            return false 