import sys

from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem,QTextEdit
from imcp import * # importation de code de l'interface
class IMC(QDialog): #(QDialog) permet l'héritage de QDialog
    def __init__(self):
        super().__init__() # applé le constructeur de l'interface
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btn.clicked.connect(self.affichage)
        self.show()
    def indicemc(self,taille,poids):
        return poids/ (taille*taille)
    def interpretation(self,t,p):
        imcv=self.indicemc(t,p)
        if(imcv<20):
            return "maigre"
        elif(imcv<=25):
            return "ideal"
        else:
            return "surpoids"   
    def affichage(self):
        try:
            poid=float(self.ui.vpoid.toPlainText())
            taille=float(self.ui.vtaille.toPlainText())
            valeur=int(self.indicemc(taille,poid))
            remarque=self.interpretation(taille,poid)
            print("la valeur de l'indice est %s et vous êtes: %s"%(valeur,remarque))
            self.ui.indice.setText("la valeur de l'indice est %s et vous êtes: %s"%(valeur,remarque))
        except:
            self.ui.erreur.setText("les champs doivent être numériques")


        







if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = IMC()

    w.show()

    sys.exit(app.exec_())