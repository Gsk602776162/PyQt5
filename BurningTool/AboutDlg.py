# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AboutDlg.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(333, 202)
        self.label = QtWidgets.QLabel(About)
        self.label.setGeometry(QtCore.QRect(70, 50, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(About)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(About)
        self.label_3.setGeometry(QtCore.QRect(70, 110, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About"))
        self.label.setText(_translate("About", "Company:JingXun Soft"))
        self.label_2.setText(_translate("About", "Version:1.0"))
        self.label_3.setText(_translate("About", "Data:2019-04-09"))

