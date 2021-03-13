import sys

from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem,QTextEdit
from rdvp import * # importation de code de l'interface
class welcome(QDialog): #(QDialog) permet l'héritage de QDialog
    def __init__(self):
        super().__init__() # applé le constructeur de l'interface
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.save.clicked.connect(self.tester)
        self.ui.cancel.clicked.connect(self.vider)
        self.show()
    def tester(self):
        print("ok")
        date=self.ui.date.toPlainText()
        duree=self.ui.Duree.toPlainText()
        description=self.ui.Description.toPlainText()
        organisation=self.ui.organisation.toPlainText()
        lieu=self.ui.Lieu.toPlainText()
        if(date==""):
            self.ui.errreur.setText(" la date est obligatoire!")

    def vider(self):
        print("vider")
        self.ui.date.setText("")
        self.ui.Duree.setText("")
        self.ui.Description.setText("")
        self.ui.organisation.setText("")
        self.ui.Lieu.setText("")




if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = welcome()

    w.show()

    sys.exit(app.exec_())