from PyQt5.QtWidgets import *
from BurningToolDlg import Ui_MainWindow
import sys
from PyQt5.QtCore import *


class MainDlgSlot(Ui_MainWindow):
    def __init__(self):
        return

    def DlgInitial(self):
        self.StartBurningButton.clicked.connect(self.StartBurning)
        self.DetectPortButton.clicked.connect(self.DetectPort)
        self.OpenPortButton.clicked.connect(self.OpenPort)
        connect(self.actionpic8,SINGAL(triggered()),this,SLOT(SetPic8()))
        #self.menubar.addAction(self.actionpic8,this,SLOT(SetPic8()))
        #self.actionpic8.setChecked.connect(self.SetPic8)
        #self.actionpic16.setChecked.connect(self.SetPic16)
        self.actionpic8.setCheckable(True)
        self.actionpic8.setChecked(True)
        self.actionpic16.setCheckable(True)
        return

    def StartBurning(self):
        self.lineEditMac1.setText("success")
        QApplication.processEvents()
        return

    def DetectPort(self):
        return

    def OpenPort(self):
        return

    def MenuSet(self):
        return

    def MenuAbout(self):
        return

    def SetPic8(self):
        self.actionpic16.setChecked(False)
        self.actionpic8.setChecked(True)
        return

    def SetPic16(self):
        self.actionpic8.setChecked(False)
        self.actionpic16.setChecked(True)
        return