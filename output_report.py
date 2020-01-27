import sys
from PyQt5 import QtCore, QtWidgets,QtGui
from Ui_base import Ui_MainWindow

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

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
        Ui_MainWindow.__init__(self)
        self.setupUi(self.dialog)

    def SaveAsPDF(self,loc):
        self.centralwidget.SaveAsPDF(loc)

    def show(self):
        self.dialog.show()
        self.app.exec_()









    def _add_figure(self,figure,layout):
        widget=QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)

        canvas = FigureCanvas( figure)
        canvas.setObjectName("page_"+str(self.count()+1))


        toolbar=NavigationToolbar(canvas, self)

        layout.addWidget(canvas)
        layout.addWidget(toolbar)

        self.addWidget(widget)





