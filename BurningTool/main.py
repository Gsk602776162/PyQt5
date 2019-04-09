import sys
import BurningToolDlg
from BurningTool import MainDlgSlot
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QPushButton
from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    QtWidgets.QDialog
    ui = BurningToolDlg.Ui_MainWindow()
    ui = MainDlgSlot()


    ui.setupUi(MainWindow)
    ui.DlgInitial()
    MainWindow.show()
    sys.exit(app.exec_())