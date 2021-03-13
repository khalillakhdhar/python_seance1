import sys

from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem,QTextEdit
from rdvp import * # importation de code de l'interface
class welcome(QDialog): #(QDialog) permet l'héritage de QDialog
    def __init__(self):
        super().__init__() # applé le constructeur de l'interface
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.save.clicked.connect(self.tester)
        self.ui.save.clicked.connect(self.tester)
        self.show()
    def tester(self):
        print("ok")
    def vider(self):
        print("vider")
        self.ui.date.setText("")
        self.ui.duree.setText("")
        self.ui.description.setText("")
        self.ui.organisation.setText("")
        self.ui.Lieu.setText("")




if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = welcome()

    w.show()

    sys.exit(app.exec_())