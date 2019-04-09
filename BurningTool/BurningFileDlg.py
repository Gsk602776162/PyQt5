# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BurningFileDlg.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BurningFile(object):
    def setupUi(self, BurningFile):
        BurningFile.setObjectName("BurningFile")
        BurningFile.resize(577, 361)
        self.label = QtWidgets.QLabel(BurningFile)
        self.label.setGeometry(QtCore.QRect(40, 110, 54, 12))
        self.label.setObjectName("label")
        self.comboBoxBurnFile = QtWidgets.QComboBox(BurningFile)
        self.comboBoxBurnFile.setGeometry(QtCore.QRect(100, 100, 331, 22))
        self.comboBoxBurnFile.setObjectName("comboBoxBurnFile")
        self.toolButtonBurnFile = QtWidgets.QToolButton(BurningFile)
        self.toolButtonBurnFile.setGeometry(QtCore.QRect(440, 100, 37, 18))
        self.toolButtonBurnFile.setObjectName("toolButtonBurnFile")

        self.retranslateUi(BurningFile)
        QtCore.QMetaObject.connectSlotsByName(BurningFile)

    def retranslateUi(self, BurningFile):
        _translate = QtCore.QCoreApplication.translate
        BurningFile.setWindowTitle(_translate("BurningFile", "BurningFile"))
        self.label.setText(_translate("BurningFile", "烧录文件："))
        self.toolButtonBurnFile.setText(_translate("BurningFile", "..."))

