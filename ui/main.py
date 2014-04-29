# -*- coding: utf-8 -*-

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature

from helper import process_command
from ui.Ui_main import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

    @pyqtSignature("")
    def on_pushButton_clicked(self):
        self.textBrowser.setText(process_command(self, self.lineEdit.text()))

    @pyqtSignature("")
    def on_lineEdit_returnPressed(self):
        self.on_pushButton_clicked()
