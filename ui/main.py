#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import QMainWindow, QFileDialog
from PyQt4.QtCore import pyqtSignature

from mod_file import load_info
from ui.Ui_main import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def show_cmf_info(self):
        mod = load_info(self.modFile.text())
        display_text = []
        display_text += mod.name.text
        display_text += " (" + mod.version.get("format").format(
            *mod.version.getchildren()) + ")"
        display_text += " by " + mod.author.text
        display_text += "\n\n" + mod.shortDesc.text
        display_text += "\n\n" + mod.homepage.text
        display_text += "\n\n----------------------------------------"
        display_text += "---------------------------------------"
        display_text += "\n\n" + mod.desc.text
        display_text += "\n\n----------------------------------------"
        display_text += "---------------------------------------"
        display_text += "\n\nChangelog:"
        for entry in mod.changelog.entry:
            display_text += "\n\n{} ({}):\n{}".format(
                entry.get("version"), entry.get("date"), entry.text)
        display_text += "\n\n----------------------------------------"
        display_text += "---------------------------------------"
        display_text += "\n\nAdds:"
        try:
            for add in mod.files.add:
                display_text += "\n" + add.text
        except TypeError:
            display_text += "\nnothing"
        display_text += "\n\nModifies:"
        try:
            for modify in mod.files.modify:
                display_text += "\n" + modify.text
        except TypeError:
            display_text += "\nnothing"
        display_text += "\n\nReplaces:"
        try:
            for replace in mod.files.replace:
                display_text += "\n" + replace.text
        except TypeError:
            display_text += "\nnothing"
        self.out.setText("".join(display_text))

    @pyqtSignature("")
    def on_lineEdit_returnPressed(self):
        self.on_pushButton_clicked()

    @pyqtSignature("")
    def on_installButton_clicked(self):
        pass

    @pyqtSignature("")
    def on_modFile_returnPressed(self):
        self.show_cmf_info()

    @pyqtSignature("")
    def on_modFileButton_clicked(self):
        file_name = QFileDialog.getOpenFileName(
            self, filter="Crea Mod File (*.cmf)")
        self.modFile.setText(file_name)
        self.show_cmf_info()

    @pyqtSignature("")
    def on_creaPath_returnPressed(self):
        pass

    @pyqtSignature("")
    def on_creaPathButton_clicked(self):
        pass
