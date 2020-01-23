# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\jlumpkin\OneDrive\output_report\base.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport

class MainWidget(QtWidgets.QWidget):
    def __init__(self,parent):
        QtWidgets.QWidget.__init__(self,parent)

    def SaveAsPDF(self,loc):
        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
        printer.setPageSize(QtPrintSupport.QPrinter.A9)
        printer.setColorMode(QtPrintSupport.QPrinter.Color)
        printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
        printer.setOutputFileName(loc)
        self.render(printer)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 681)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = MainWidget(self.centralwidget)
        self.widget.setAutoFillBackground(False)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 840, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_PDF = QtWidgets.QAction(MainWindow)
        self.actionSave_PDF.setObjectName("actionSave_PDF")
        self.actionTEST = QtWidgets.QAction(MainWindow)
        self.actionTEST.setObjectName("actionTEST")
        self.menuOptions.addAction(self.actionSave_PDF)
        self.menuOptions.addAction(self.actionTEST)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionSave_PDF.setText(_translate("MainWindow", "Save PDF"))
        self.actionTEST.setText(_translate("MainWindow", "TEST"))

