# -*- coding: utf-8 -*-

"""
Module implementing Main.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature, QProcess

from Ui_main import Ui_MainWindow,  _translate


class Main(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        process = QProcess(self)
        process.start(self.lineEdit.text())
        process.waitForFinished()
        self.textBrowser.setText(process.readAllStandardOutput().data())

    @pyqtSignature("")
    def on_lineEdit_returnPressed(self):
        """
        Slot documentation goes here.
        """
        self.on_pushButton_clicked()
