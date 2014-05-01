# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\GitHub\Crea-Mod-Manager\ui\main.ui'
#
# Created: Thu May 01 23:06:44 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(532, 474)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.installButton = QtGui.QPushButton(self.centralWidget)
        self.installButton.setGeometry(QtCore.QRect(430, 10, 87, 27))
        self.installButton.setObjectName(_fromUtf8("installButton"))
        self.modFile = QtGui.QLineEdit(self.centralWidget)
        self.modFile.setGeometry(QtCore.QRect(70, 10, 331, 24))
        self.modFile.setObjectName(_fromUtf8("modFile"))
        self.out = QtGui.QTextBrowser(self.centralWidget)
        self.out.setGeometry(QtCore.QRect(10, 80, 512, 384))
        self.out.setObjectName(_fromUtf8("out"))
        self.modFileButton = QtGui.QToolButton(self.centralWidget)
        self.modFileButton.setGeometry(QtCore.QRect(400, 10, 26, 22))
        self.modFileButton.setObjectName(_fromUtf8("modFileButton"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 11, 51, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 43, 58, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.creaPath = QtGui.QLineEdit(self.centralWidget)
        self.creaPath.setGeometry(QtCore.QRect(70, 40, 331, 24))
        self.creaPath.setObjectName(_fromUtf8("creaPath"))
        self.creaPathButton = QtGui.QToolButton(self.centralWidget)
        self.creaPathButton.setGeometry(QtCore.QRect(400, 40, 26, 22))
        self.creaPathButton.setObjectName(_fromUtf8("creaPathButton"))
        self.uninstallButton = QtGui.QPushButton(self.centralWidget)
        self.uninstallButton.setGeometry(QtCore.QRect(430, 40, 87, 27))
        self.uninstallButton.setObjectName(_fromUtf8("uninstallButton"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Crea Mod Manager", None))
        self.installButton.setText(_translate("MainWindow", "Install", None))
        self.modFileButton.setText(_translate("MainWindow", "...", None))
        self.label.setText(_translate("MainWindow", "Mod file", None))
        self.label_2.setText(_translate("MainWindow", "Crea path", None))
        self.creaPathButton.setText(_translate("MainWindow", "...", None))
        self.uninstallButton.setText(_translate("MainWindow", "Uninstall", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

