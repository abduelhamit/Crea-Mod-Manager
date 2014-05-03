#!/usr/bin/python
# -*- coding: utf-8 -*-

from lxml.etree import XMLSyntaxError
from PyQt4.QtGui import (
    QMainWindow, QFileDialog, QMessageBox, QStandardItem, QStandardItemModel)
from PyQt4.QtCore import pyqtSignature, QModelIndex, QFile

from core.mod_file import load_info, parse_info
from core.ModManager import ModManager
from ui.Ui_main import Ui_MainWindow
from ModListView import ModListView


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # instantiate our self.manager singleton
        self.manager = ModManager()
        # ModListView.currentChanged() will emit
        # the 'current_mod_changed' signal
        self.installedMods.current_mod_changed.connect(
            self.update_current_mod)

    def is_current_mod_in_installed_list(self):
        return self.manager.is_mod_installed(
            installed_list = \
            [str(self.installedMods.model().item(i).text()) for i in
             xrange(self.installedMods.model().rowCount())])

    def update_mod_text(self, path=None):
        try:
            if path is None:
                info_text = parse_info(self.manager.current_mod)
            else:
                info_text = parse_info(load_info(path))
            self.out.setText(info_text)
            return True
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

    def update_current_mod(self, index):
        self.manager.update_current_mod(
            str(index.data().toString())
        )
        self.update_mod_text()
    
    def new_current_mod(self, path):
        self.manager.new_current_mod(str(path))
        self.modFile.setText(path)
        self.update_mod_text()

    @pyqtSignature("")
    def on_lineEdit_returnPressed(self):
        self.on_pushButton_clicked()

    def add_mod_to_list(self, mod=None):
        if mod is None:
            mod = self.manager.current_mod
        self.installedMods.model().appendRow(
            QStandardItem(self.manager.get_mod_name(mod)))

    def refresh_mod_list(self):
        # remove all rows
        print self.manager.installed_mods
        self.installedMods.model().removeRows(
            0, self.installedMods.model().rowCount())
        # and re-add installed mods
        for mod in self.manager.installed_mods.values():
            self.add_mod_to_list(mod)

    @pyqtSignature("")
    def on_installButton_clicked(self):
        # if we haven't already installed the mod
        if not self.is_current_mod_in_installed_list():
            # add its name to the installed list
            self.add_mod_to_list()
            # and install it
            self.manager.install()

    @pyqtSignature("")
    def on_uninstallButton_clicked(self):
        if len(self.manager.installed_mods) > 0:
            if self.is_current_mod_in_installed_list():
                self.check_crea_path(self.creaPath.text())
                # uninstall the mod
                self.manager.uninstall()
                # and remove it from the installed list
                self.installedMods.model().removeRow(
                    self.installedMods.model().indexFromItem(
                        self.installedMods.model().findItems(
                            self.manager.get_mod_name()
                        )[0]
                    ).row()
                )
    
    @pyqtSignature("")
    def on_saveButton_clicked(self):
        self.manager.save_mod_list()
    
    @pyqtSignature("")
    def on_loadButton_clicked(self):
        self.manager.load_mod_list()
        self.refresh_mod_list()

    @pyqtSignature("")
    def on_modFile_returnPressed(self):
        self.update_mod_text(self.modFile.text())

    @pyqtSignature("")
    def on_modFileButton_clicked(self):
        file_name = QFileDialog.getOpenFileName(
            self, filter="Crea Mod File (*.cmf)")
        if not file_name or not self.update_mod_text(str(file_name)):
            return
        else:
            self.new_current_mod(file_name)

    def check_crea_path(self, path):
        if not QFile.exists(path + "/Crea") and not QFile.exists(
                path + "\\Crea.exe"):
            QMessageBox.critical(self, "Crea Path Error", "Crea not found.")
            return False
        return True

    @pyqtSignature("")
    def on_creaPath_returnPressed(self):
        self.check_crea_path(self.creaPath.text())

    @pyqtSignature("")
    def on_creaPathButton_clicked(self):
        crea_path = QFileDialog.getExistingDirectory(self)
        if not crea_path or not self.check_crea_path(crea_path):
            return
        self.creaPath.setText(crea_path)
