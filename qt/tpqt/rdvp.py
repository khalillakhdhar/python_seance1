# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rdvui.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(613, 608)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 150, 47, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 210, 47, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 270, 91, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 350, 61, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 410, 101, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(260, 50, 91, 21))
        self.label_6.setObjectName("label_6")
        self.save = QtWidgets.QPushButton(Dialog)
        self.save.setGeometry(QtCore.QRect(250, 520, 75, 23))
        self.save.setObjectName("save")
        self.cancel = QtWidgets.QPushButton(Dialog)
        self.cancel.setGeometry(QtCore.QRect(370, 520, 75, 23))
        self.cancel.setObjectName("cancel")
        self.errreur = QtWidgets.QLabel(Dialog)
        self.errreur.setGeometry(QtCore.QRect(90, 480, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.errreur.setFont(font)
        self.errreur.setObjectName("errreur")
        self.date = QtWidgets.QTextEdit(Dialog)
        self.date.setGeometry(QtCore.QRect(140, 140, 251, 41))
        self.date.setObjectName("date")
        self.Lieu = QtWidgets.QTextEdit(Dialog)
        self.Lieu.setGeometry(QtCore.QRect(140, 200, 251, 41))
        self.Lieu.setObjectName("Lieu")
        self.Description = QtWidgets.QTextEdit(Dialog)
        self.Description.setGeometry(QtCore.QRect(140, 250, 251, 61))
        self.Description.setObjectName("Description")
        self.Duree = QtWidgets.QTextEdit(Dialog)
        self.Duree.setGeometry(QtCore.QRect(140, 340, 251, 41))
        self.Duree.setObjectName("Duree")
        self.organisation = QtWidgets.QTextEdit(Dialog)
        self.organisation.setGeometry(QtCore.QRect(140, 400, 251, 71))
        self.organisation.setObjectName("organisation")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">date</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Lieu</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Description</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Duree</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">organisation</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; color:#ff0000;\">fiche rdv</span></p></body></html>"))
        self.save.setText(_translate("Dialog", "save"))
        self.cancel.setText(_translate("Dialog", "cancel"))
        self.errreur.setText(_translate("Dialog", "TextLabel"))
