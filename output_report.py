import sys
from PyQt5 import QtCore, QtWidgets,QtGui
from Ui_base import Ui_MainWindow


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s



class Page(Ui_MainWindow):

    def __init__(self):
        self.app=0
        self.app = QtWidgets.QApplication([])
        self.dialog = QtWidgets.QMainWindow()
        #prog = MainWindow(self.dialog)



        Ui_MainWindow.__init__(self)
        self.setupUi(self.dialog)


    def show(self):
        self.dialog.show()
        self.app.exec_()