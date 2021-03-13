import sys

from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem,QTextEdit
from imcp import * # importation de code de l'interface
class IMC(QDialog): #(QDialog) permet l'héritage de QDialog
    def __init__(self):
        super().__init__() # applé le constructeur de l'interface
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.show()





if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = IMC()

    w.show()

    sys.exit(app.exec_())