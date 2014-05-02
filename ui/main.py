#!/usr/bin/python
# -*- coding: utf-8 -*-

from lxml.etree import XMLSyntaxError
from PyQt4.QtGui import QMainWindow, QFileDialog, QMessageBox, QStandardItem
from PyQt4.QtCore import pyqtSignature, SIGNAL, QModelIndex

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
        self.installed_mods_data = {}
        self.installedMods = ModListView()
        # ModListView.currentChanged() will send
        # the 'current_mod_changed' signal
        self.connect(self, SIGNAL('current_mod_changed'),
                     self.update_current_mod)

    def is_current_mod_in_installed_list(self):
        print [str(self.installedMods.model().item(i).text()) for i in
                     xrange(self.installedMods.model().rowCount())]
        if self.current_mod is not None:
            return self.current_mod.name.text in \
                [row for row in
                    [str(self.installedMods.model().item(i).text()) for i in
                     xrange(self.installedMods.model().rowCount())]
                ]
        return False

    def update_mod_text(self, path=None):
        if path is None:
            info_text = parse_info(self.current_mod)
        else:
            info_text = parse_info(load_info(self.modFile.text()))
        self.out.setText(info_text)

    def update_current_mod(self, current_index):
        # retrieve the mod data using the mod name
        self.current_mod = self.installed_mods_data[current_index.data()]
        self.update_mod_text()

    def reset_model(self):
        self.installedMods.setModel(self.installedMods.model())

    @pyqtSignature("")
    def on_lineEdit_returnPressed(self):
        self.on_pushButton_clicked()

    @pyqtSignature("")
    def on_installButton_clicked(self):
        # if we haven't already installed the mod
        if not self.is_current_mod_in_installed_list():
            # install the mod
            # TODO: install
            # and add it to the installed list
            #self.installedMods.model().beginInsertRows(
            #    QModelIndex(),
            #    self.installedMods.model().rowCount(),
            #    self.installedMods.model().rowCount())
            self.installedMods.model().appendRow(
                QStandardItem(self.current_mod.name.text))
            #self.installedMods.model().endInsertRows()
            #for i in (self.installedMods.model().createIndex(j, 0) for j in xrange(self.installedMods.model().rowCount())):
            #    self.installedMods.update(i)
            self.reset_model()

    @pyqtSignature("")
    def on_uninstallButton_clicked(self):
        if self.installedMods.model().rowCount() > 0:
            if self.is_current_mod_in_installed_list():
                # uninstall the mod
                # TODO: uninstall
                # and remove it from the installed list
                index = self.installedMods.model().indexFromItem(
                        self.installedMods.model().findItems(
                        self.current_mod.name.text)[0]
                    ).row()
                #self.installedMods.model().beginRemoveRows(
                #    QModelIndex(), index, index)
                self.installedMods.model().removeRow(index)
                #self.installedMods.model().endRemoveRows()

    @pyqtSignature("")
    def on_modFile_returnPressed(self):
        try:
            update_mod_text(self.modFile.text())
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

    @pyqtSignature("")
    def on_modFileButton_clicked(self):
        file_name = QFileDialog.getOpenFileName(
            self, filter="Crea Mod File (*.cmf)")
        if not file_name:
            return
        try:
            self.current_mod = load_info(file_name)
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
        self.modFile.setText(file_name)

    @pyqtSignature("")
    def on_creaPath_returnPressed(self):
        pass

    @pyqtSignature("")
    def on_creaPathButton_clicked(self):
        pass
