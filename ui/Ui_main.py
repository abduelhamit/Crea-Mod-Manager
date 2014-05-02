# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Fri May 02 13:11:37 2014
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
        MainWindow.resize(750, 475)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(750, 475))
        MainWindow.setMaximumSize(QtCore.QSize(750, 475))
        self.centralWidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.installButton = QtGui.QPushButton(self.centralWidget)
        self.installButton.setGeometry(QtCore.QRect(430, 10, 87, 27))
        self.installButton.setObjectName(_fromUtf8("installButton"))
        self.modFile = QtGui.QLineEdit(self.centralWidget)
        self.modFile.setGeometry(QtCore.QRect(70, 10, 331, 24))
        self.modFile.setObjectName(_fromUtf8("modFile"))
        self.out = QtGui.QTextBrowser(self.centralWidget)
        self.out.setGeometry(QtCore.QRect(10, 80, 512, 381))
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
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(600, 10, 71, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.installedMods = ModListView(self.centralWidget)
        self.installedMods.setGeometry(QtCore.QRect(535, 30, 201, 431))
        self.installedMods.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.installedMods.setLayoutMode(QtGui.QListView.SinglePass)
        self.installedMods.setObjectName(_fromUtf8("installedMods"))
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
        self.label_3.setText(_translate("MainWindow", "Installed Mods", None))

from ModListView import ModListView
