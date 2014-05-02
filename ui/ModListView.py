#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import pyqtSignal, QModelIndex
from PyQt4.QtGui import QListView, QStandardItemModel, QStandardItem

class ModListView(QListView):
    
    current_mod_changed = pyqtSignal(QModelIndex)
    
    def __init__(self, parent=None):
        QListView.__init__(self, parent)
        self.setModel(QStandardItemModel())
        
    def currentChanged(self, current, previous):
        QListView.currentChanged(self, current, previous)
        self.current_mod_changed.emit(current)
