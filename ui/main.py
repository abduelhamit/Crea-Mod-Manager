#!/usr/bin/python
# -*- coding: utf-8 -*-

from lxml.etree import XMLSyntaxError
from PyQt4.QtGui import QMainWindow, QFileDialog, QMessageBox
from PyQt4.QtCore import pyqtSignature

from mod_file import parse_info
from ui.Ui_main import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

    @pyqtSignature("")
    def on_lineEdit_returnPressed(self):
        self.on_pushButton_clicked()

    @pyqtSignature("")
    def on_installButton_clicked(self):
        pass

    def set_info_text(self, path):
        try:
            info_text = parse_info(path)
        except (XMLSyntaxError) as error:
            if error.message:
                message = error.message
            else:
                message = "Unknown error"
            QMessageBox.critical(
                self, "CMF Parsing Error",
                "Oops. Something went wrong while opening the CMF:\n{}".format(
                    message))
            return
        self.out.setText(info_text)

    @pyqtSignature("")
    def on_modFile_returnPressed(self):
        self.set_info_text(self.modFile.text())

    @pyqtSignature("")
    def on_modFileButton_clicked(self):
        file_name = QFileDialog.getOpenFileName(
            self, filter="Crea Mod File (*.cmf)")
        if not file_name:
            return
        self.set_info_text(file_name)
        self.modFile.setText(file_name)

    @pyqtSignature("")
    def on_creaPath_returnPressed(self):
        pass

    @pyqtSignature("")
    def on_creaPathButton_clicked(self):
        pass
