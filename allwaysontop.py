# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
from PyQt5 import QtCore

from PyQt5.QtWidgets import QPushButton,QGridLayout,QPlainTextEdit,QFileDialog,QWidget,QApplication,QMainWindow,QVBoxLayout
from PyQt5.QtCore import pyqtSignal,Qt,QObject
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Ui_Form(QMainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, Form):

        Form.resize(500, 500)
        Form.setWindowIcon(QIcon('pavi.png'))
        Form.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SAVE = QtWidgets.QPushButton(Form)
        self.SAVE.setMinimumSize(QtCore.QSize(0, 25))
        self.SAVE.setObjectName("SAVE")
        self.horizontalLayout.addWidget(self.SAVE)
        self.LOAD = QtWidgets.QPushButton(Form)
        self.LOAD.setMinimumSize(QtCore.QSize(0, 25))
        self.LOAD.setObjectName("LOAD")
        self.horizontalLayout.addWidget(self.LOAD)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.SAVE.clicked.connect(self.saveme)
        self.LOAD.clicked.connect(self.saveme1)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def saveme(self):
        texted = self.plainTextEdit.toPlainText()
        FileSave = QFileDialog.getSaveFileName(self, 'Save file','', " text (*.txt);;")
        if FileSave[0] == '':
           pass
        else:

            f = open((FileSave[0]), 'w', -1, "utf-8")
            f.write(texted)
            f.close()


    def saveme1(self):

        FileSave = QFileDialog.getOpenFileName(self, 'Save file','', " text (*.txt);;")
        if FileSave[0] == '':
           pass
        else:

            f = open((FileSave[0]), 'r', -1, "utf-8")
            data = f.read()
            f.close()
            self.plainTextEdit.setPlainText(data)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ontop"))
        self.SAVE.setText(_translate("Form", "SAVE"))
        self.LOAD.setText(_translate("Form", "LOAD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
