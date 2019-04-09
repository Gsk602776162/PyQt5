from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog
from BurningToolDlg import Ui_MainWindow
from BurningFileDlg import Ui_BurningFile
from AboutDlg import Ui_About
from PyQt5.QtWidgets import QAction
import sys
from PyQt5.QtCore import *
import serial
import time


class MainDlgSlot(Ui_MainWindow,Ui_BurningFile,Ui_About):
    def __init__(self):
        self.COMPortList = ['COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8','COM9','COM10',
                            'COM11', 'COM12', 'COM13', 'COM14', 'COM15', 'COM16', 'COM17', 'COM18', 'COM19', 'COM20',
                            'COM21', 'COM22', 'COM23', 'COM24', 'COM25', 'COM26', 'COM27', 'COM28', 'COM29', 'COM30',
                            'COM31', 'COM32', 'COM33', 'COM34', 'COM35', 'COM36', 'COM37', 'COM38', 'COM39', 'COM40',
                            'COM41', 'COM42', 'COM43', 'COM44', 'COM45', 'COM46', 'COM47', 'COM48', 'COM49', 'COM50',
                            'COM51', 'COM52', 'COM53', 'COM54', 'COM55', 'COM56', 'COM57', 'COM58', 'COM59', 'COM60',
                            'COM61', 'COM62', 'COM63', 'COM64']

        self.child = BurningFile()
        self.about = About()
        return

    def DlgInitial(self):
        self.StartBurningButton.clicked.connect(self.StartBurning)
        self.DetectPortButton.clicked.connect(self.DetectPort)
        self.OpenPortButton.clicked.connect(self.OpenPort)
        self.actionpic8.triggered.connect(self.SetPic8)
        self.SetFileSubMenu.triggered.connect(self.OpenBurningFileDlg)
        self.menuAbout.triggered.connect(self.OpenAboutDlg)
        self.actionpic16.triggered.connect(self.SetPic16)

        self.comboBox1.hide()
        self.comboBox2.hide()
        self.comboBox3.hide()
        self.comboBox4.hide()
        self.comboBox5.hide()
        self.comboBox6.hide()
        self.comboBox7.hide()
        self.comboBox8.hide()
        self.comboBox9.hide()
        self.comboBox10.hide()
        self.comboBox11.hide()
        self.comboBox12.hide()
        self.comboBox13.hide()
        self.comboBox14.hide()
        self.comboBox15.hide()
        self.comboBox16.hide()
        return

    def StartBurning(self):
        self.lineEditMac1.setText("success")
        QApplication.processEvents()
        return

    def DetectPort(self):
        AccessCOMList = []
        for i in range(0, 64):
            try:
                ser = serial.Serial(port=self.COMPortList[i], baudrate=38400, parity=serial.PARITY_NONE,bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE)
            except:
                continue
            else:
                ser.close()
                AccessCOMList.append(self.COMPortList[i])
        self.comboBox1.addItems(AccessCOMList)
        self.comboBox1.show()
        self.comboBox2.addItems(AccessCOMList)
        self.comboBox2.setCurrentIndex(1)
        self.comboBox2.show()
        self.comboBox3.addItems(AccessCOMList)
        self.comboBox3.show()
        self.comboBox4.addItems(AccessCOMList)
        self.comboBox4.show()
        self.comboBox5.addItems(AccessCOMList)
        self.comboBox5.show()
        self.comboBox6.addItems(AccessCOMList)
        self.comboBox6.show()
        self.comboBox7.addItems(AccessCOMList)
        self.comboBox7.show()
        self.comboBox8.addItems(AccessCOMList)
        self.comboBox8.show()
        self.comboBox9.addItems(AccessCOMList)
        self.comboBox9.show()
        self.comboBox10.addItems(AccessCOMList)
        self.comboBox10.show()
        self.comboBox11.addItems(AccessCOMList)
        self.comboBox11.show()
        self.comboBox12.addItems(AccessCOMList)
        self.comboBox12.show()
        self.comboBox13.addItems(AccessCOMList)
        self.comboBox13.show()
        self.comboBox14.addItems(AccessCOMList)
        self.comboBox14.show()
        self.comboBox15.addItems(AccessCOMList)
        self.comboBox15.show()
        self.comboBox16.addItems(AccessCOMList)
        self.comboBox16.show()

        self.labelstate1.setText('Ready')
        self.labelstate2.setText('Ready')
        self.labelstate3.setText('Ready')
        self.labelstate4.setText('Ready')
        self.labelstate5.setText('Ready')
        self.labelstate6.setText('Ready')
        self.labelstate7.setText('Ready')
        self.labelstate8.setText('Ready')
        self.labelstate9.setText('Ready')
        self.labelstate10.setText('Ready')
        self.labelstate11.setText('Ready')
        self.labelstate12.setText('Ready')
        self.labelstate13.setText('Ready')
        self.labelstate14.setText('Ready')
        self.labelstate15.setText('Ready')
        self.labelstate16.setText('Ready')
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
        self.labelportcombo9.hide()
        self.labelportcombo10.hide()
        self.labelportcombo11.hide()
        self.labelportcombo12.hide()
        self.labelportcombo13.hide()
        self.labelportcombo14.hide()
        self.labelportcombo15.hide()
        self.labelportcombo16.hide()
        self.progressBar9.hide()
        self.progressBar10.hide()
        self.progressBar11.hide()
        self.progressBar12.hide()
        self.progressBar13.hide()
        self.progressBar14.hide()
        self.progressBar15.hide()
        self.progressBar16.hide()
        return

    def SetPic16(self):
        self.actionpic8.setChecked(False)
        self.actionpic16.setChecked(True)
        self.labelportcombo9.show()
        self.labelportcombo10.show()
        self.labelportcombo11.show()
        self.labelportcombo12.show()
        self.labelportcombo13.show()
        self.labelportcombo14.show()
        self.labelportcombo15.show()
        self.labelportcombo16.show()
        self.progressBar9.show()
        self.progressBar10.show()
        self.progressBar11.show()
        self.progressBar12.show()
        self.progressBar13.show()
        self.progressBar14.show()
        self.progressBar15.show()
        self.progressBar16.show()
        return

    def OpenBurningFileDlg(self):
        self.child.show()
        self.child.DlgInitial()
        return

    def OpenAboutDlg(self):
        self.about.show()
        return

class BurningFile(QMainWindow,Ui_BurningFile):
    def __init__(self):
        super(BurningFile,self).__init__()
        self.setupUi(self)

    def DlgInitial(self):
        self.toolButtonBurnFile.clicked.connect(self.ScanBurnFile)
        return

    def ScanBurnFile(self):
        file_path = QFileDialog.getOpenFileName()
        self.App_File = file_path[0]
        mark = 0
        for i in range(len(self.App_File)):
            if self.App_File[i] == '/':
                mark = i + 1
        file_name = self.App_File[mark:len(self.App_File)]
        self.comboBoxBurnFile.addItem(file_name)
        path = sys.path
        self.App_File = path[0] + '\\' + file_name

class About(QMainWindow,Ui_About):
    def __init__(self):
        super(About,self).__init__()
        self.setupUi(self)