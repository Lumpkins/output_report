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
        # printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
        # printer.setPageSize(QtPrintSupport.QPrinter.A9)
        # printer.setColorMode(QtPrintSupport.QPrinter.Color)
        # printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
        # printer.setOutputFileName(loc)
        # self.render(printer)

        # printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
        # printer.setPageSize(QtPrintSupport.QPrinter.A6)
        # printer.setColorMode(QtPrintSupport.QPrinter.Color)
        # printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
        # printer.setOutputFileName(loc)
        # pixmap = QtPrintSupport.QPixmap.grabWidget(self).scaled(
        #     printer.pageRect(QtPrintSupport.QPrinter.DevicePixel).size().toSize(),
        #     QtCore.Qt.KeepAspectRatio)
        # painter = QtPrintSupport.QPainter(printer)
        # painter.drawPixmap(0, 0, pixmap)
        # painter.end()

        printer = QtPrintSupport.QPrinter()
        printer.setPageSize(QtPrintSupport.QPrinter.Letter)
        dpi=self.width()/8
        print(self.width())
        printer.setResolution(dpi)
        printer.setColorMode(QtPrintSupport.QPrinter.Color)
        printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
        printer.setOutputFileName(loc)
        size = printer.pageRect(QtPrintSupport.QPrinter.DevicePixel).size()
        pixmap =self.grab() 
        #QtGui.QScreen.grabWidget(self).scaled(size.toSize(), QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation)
        data = QtCore.QByteArray()
        buffer = QtCore.QBuffer(data)
        pixmap.save(buffer, 'PNG')
        document = QtGui.QTextDocument()
        document.setPageSize(size)
        document.setHtml('<img src="data:image/png;base64,%s"/>' %
                         bytes(data.toBase64()).decode('ascii'))
        document.print_(printer)





class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 681)
        self.centralwidget = MainWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

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
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(self.sizePolicy)
        self.sizePolicy.setHeightForWidth(True)
        
    def heightForWidth(self, width):
        return width * 11/8.5

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionSave_PDF.setText(_translate("MainWindow", "Generate PDF"))
        self.actionTEST.setText(_translate("MainWindow", "TEST"))

