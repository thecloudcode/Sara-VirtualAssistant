# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SaraUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(795, 603)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 611))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Downloads/LCPT.gif"))
        self.label.setObjectName("label")
        self.startbutton = QtWidgets.QPushButton(Dialog)
        self.startbutton.setGeometry(QtCore.QRect(30, 230, 93, 28))
        self.startbutton.setStyleSheet("border-color: rgb(0, 243, 255);\n"
"background-color: rgb(0, 110, 116);")
        self.startbutton.setObjectName("startbutton")
        self.stopbutton = QtWidgets.QPushButton(Dialog)
        self.stopbutton.setGeometry(QtCore.QRect(30, 270, 93, 28))
        self.stopbutton.setStyleSheet("background-color: rgb(22, 89, 87);")
        self.stopbutton.setObjectName("stopbutton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.startbutton.setText(_translate("Dialog", "Run"))
        self.stopbutton.setText(_translate("Dialog", "Breaka"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())