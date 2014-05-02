#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QListView, QStandardItemModel

class ModListView(QListView):
    def __init__(self, parent=None):
        QListView.__init__(self, parent)
        self.setModel(QStandardItemModel())
        
    def currentChanged(self, current, previous):
        QListView.currentChanged(self, current, previous)
        self.emit(SIGNAL('current_mod_changed'), current)
