#!/usr/bin/python
# -*- coding: utf-8 -*-

from lxml.etree import XMLSyntaxError
from PyQt4.QtGui import QMainWindow, QFileDialog, QMessageBox, \
    QStandardItem, QStandardItemModel
from PyQt4.QtCore import pyqtSignature, QModelIndex

from mod_file import load_info, parse_info
from ModManager import ModManager
from ui.Ui_main import Ui_MainWindow
from ModListView import ModListView


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # instantiate our manager singleton
        self.manager = ModManager()
        # ModListView.currentChanged() will emit
        # the 'current_mod_changed' signal
        self.installedMods.current_mod_changed.connect(
            self.update_current_mod)

    def is_current_mod_in_installed_list(self):
        return manager.is_mod_installed(
            installed_list = \
            [str(self.installedMods.model().item(i).text()) for i in
             xrange(self.installedMods.model().rowCount())])

    def update_mod_text(self, path=None):
        if path is None:
            info_text = parse_info(manager.current_mod)
        else:
            info_text = parse_info(load_info(self.modFile.text()))
        self.out.setText(info_text)

    def update_current_mod(self, current_index):
        manager.update_current_mod(
            current_index,
            lambda index: str(index.data().toString())
        )
        self.update_mod_text()

    @pyqtSignature("")
    def on_lineEdit_returnPressed(self):
        self.on_pushButton_clicked()

    @pyqtSignature("")
    def on_installButton_clicked(self):
        # if we haven't already installed the mod
        if not self.is_current_mod_in_installed_list():
            # add its name to the installed list
            self.installedMods.model().appendRow(
                QStandardItem(manager.get_mod_name()))
            # and install it
            manager.install()

    @pyqtSignature("")
    def on_uninstallButton_clicked(self):
        if len(manager.installed_mods) > 0:
            if self.is_current_mod_in_installed_list():
                # uninstall the mod
                manager.uninstall()
                # and remove it from the installed list
                self.installedMods.model().removeRow(
                    self.installedMods.model().indexFromItem(
                        self.installedMods.model().findItems(
                            manager.get_mod_name()
                        )[0]
                    ).row()
                )

    def set_info_text(self, path):
        try:
<<<<<<< HEAD
            info_text = parse_info(path)
        except (XMLSyntaxError) as error:
            if error.message:
                message = error.message
||||||| merged common ancestors
            info_text = parse_info(self.modFile.text())
        except (XMLSyntaxError) as e:
            if e.message:
                message = e.message
=======
            update_mod_text(self.modFile.text())
        except (XMLSyntaxError) as e:
            if e.message:
                message = e.message
>>>>>>> broken-modlist
            else:
                message = "Unknown error"
            QMessageBox.critical(
                self, "CMF Parsing Error",
                "Oops. Something went wrong while opening the CMF:\n{}".format(
                    message))
<<<<<<< HEAD
            return False
        self.out.setText(info_text)
        return True

    @pyqtSignature("")
    def on_modFile_returnPressed(self):
        self.set_info_text(self.modFile.text())
||||||| merged common ancestors
            return
        self.out.setText(info_text)
=======
            return
>>>>>>> broken-modlist

    @pyqtSignature("")
    def on_modFileButton_clicked(self):
        file_name = QFileDialog.getOpenFileName(
            self, filter="Crea Mod File (*.cmf)")
        if not file_name or not self.set_info_text(file_name):
            return
<<<<<<< HEAD
||||||| merged common ancestors
        try:
            info_text = parse_info(file_name)
        except (XMLSyntaxError) as e:
            if e.message:
                message = e.message
            else:
                message = "Unknown error"
            QMessageBox.critical(
                self, "CMF Parsing Error",
                "Oops. Something went wrong while opening the CMF:\n{}".format(
                    message))
            return
        self.out.setText(info_text)
=======
        try:
            manager.current_mod = load_info(file_name)
        except (XMLSyntaxError) as e:
            if e.message:
                message = e.message
            else:
                message = "Unknown error"
            QMessageBox.critical(
                self, "CMF Parsing Error",
                "Oops. Something went wrong while opening the CMF:\n{}".format(
                    message))
            return
        self.update_mod_text()
>>>>>>> broken-modlist
        self.modFile.setText(file_name)

    def check_crea_path(self, path):
        if not QFile.exists(path + "/Crea") and not QFile.exists(
                path + "\Crea.exe"):
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
