import sys

from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem,QTextEdit
from test import * # importation de code de l'interface
class welcome(QDialog): #(QDialog) permet l'héritage de QDialog
    def __init__(self):
        super().__init__() # applé le constructeur de l'interface
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.tester)
        self.show()
    def tester(self):

        self.ui.valeur.setText(self.ui.nom.toPlainText())
        #self.hide()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = welcome()

    w.show()

    sys.exit(app.exec_())