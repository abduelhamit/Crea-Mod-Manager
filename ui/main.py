#!/usr/bin/python
# -*- coding: utf-8 -*-

from lxml.etree import XMLSyntaxError
from PyQt4.QtGui import QMainWindow, QFileDialog, QMessageBox
from PyQt4.QtCore import pyqtSignature, QFile

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
            return False
        self.out.setText(info_text)
        return True

    @pyqtSignature("")
    def on_modFile_returnPressed(self):
        self.set_info_text(self.modFile.text())

    @pyqtSignature("")
    def on_modFileButton_clicked(self):
        file_name = QFileDialog.getOpenFileName(
            self, filter="Crea Mod File (*.cmf)")
        if not file_name or not self.set_info_text(file_name):
            return
        self.modFile.setText(file_name)

    def check_crea_path(self, path):
        if not QFile.exists(path + "/Crea") or not QFile.exists(
                path + "\Crea.exe"):
            QMessageBox.critical(self, "Crea Path Error", "Crea not found.")
            return False
        return True

    @pyqtSignature("")
    def on_creaPath_returnPressed(self):
        self.creaPath.setText(self.creaPath.text())

    @pyqtSignature("")
    def on_creaPathButton_clicked(self):
        crea_path = QFileDialog.getExistingDirectory(self)
        if not crea_path or not self.check_crea_path(crea_path):
            return
        self.creaPath.setText(crea_path)
