#!/usr/bin/python
# -*- coding: utf-8 -*-

from lxml.etree import XMLSyntaxError
from PyQt4.QtGui import (
    QMainWindow, QFileDialog, QMessageBox, QStandardItem, QStandardItemModel)
from PyQt4.QtCore import pyqtSignature, QModelIndex

from mod_file import load_info, parse_info
from ui.Ui_main import Ui_MainWindow
from ModListView import ModListView


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # keep data of one mod loaded
        self.current_mod = None
        # keep a dict of {mod_name: mod_data}
        # TODO: subclass Item for mod data
        # instead of keeping it in a member variable
        self.installed_mods_data = {}
        # ModListView.currentChanged() will emit
        # the 'current_mod_changed' signal
        self.installedMods.current_mod_changed.connect(self.update_current_mod)

    def is_current_mod_in_installed_list(self):
        if self.current_mod is not None:
            return self.current_mod.name.text in [row for row in [
                str(self.installedMods.model().item(i).text()) for i in xrange(
                    self.installedMods.model().rowCount())]]
        return False

    def update_mod_text(self, path=None):
        if path:
            try:
                mod = load_info(path)
            except (XMLSyntaxError) as e:
                if e.message:
                    message = e.message
                else:
                    message = "Unknown error"
                QMessageBox.critical(
                    self, "CMF Parsing Error",
                    "Oops. Something went wrong while opening the CMF:\n{}".format(
                        message))
                return False
        else:
            mod = self.current_mod
        self.out.setText(parse_info(mod))
        return mod

    def update_current_mod(self, current_index):
        # retrieve the mod data using the mod name
        self.current_mod = self.installed_mods_data[
            str(current_index.data().toString())]
        self.update_mod_text()

    @pyqtSignature("")
    def on_lineEdit_returnPressed(self):
        self.on_pushButton_clicked()

    @pyqtSignature("")
    def on_installButton_clicked(self):
        # if we haven't already installed the mod
        if not self.is_current_mod_in_installed_list():
            # install the mod
            # TODO: install
            # add its name to the installed list
            self.installedMods.model().appendRow(
                QStandardItem(self.current_mod.name.text))
            # and add its data to the data record
            self.installed_mods_data[
                self.current_mod.name.text] = self.current_mod

    @pyqtSignature("")
    def on_uninstallButton_clicked(self):
        if self.installedMods.model().rowCount() > 0:
            if self.is_current_mod_in_installed_list():
                # uninstall the mod
                # TODO: uninstall
                # and remove it from the installed list
                self.installedMods.model().removeRow(
                    self.installedMods.model().indexFromItem(
                        self.installedMods.model().findItems(
                            self.current_mod.name.text)[0]).row())

    @pyqtSignature("")
    def on_modFile_returnPressed(self):
        self.update_mod_text(self.modFile.text())

    @pyqtSignature("")
    def on_modFileButton_clicked(self):
        file_name = QFileDialog.getOpenFileName(
            self, filter="Crea Mod File (*.cmf)")
        if not file_name:
            return

        mod = self.update_mod_text(file_name)
        if not mod:
            return

        self.current_mod = mod
        self.modFile.setText(file_name)

    @pyqtSignature("")
    def on_creaPath_returnPressed(self):
        pass

    @pyqtSignature("")
    def on_creaPathButton_clicked(self):
        pass
