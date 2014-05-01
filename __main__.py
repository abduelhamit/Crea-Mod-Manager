#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv

from PyQt4.QtGui import QApplication

from ui.main import Main


APP = QApplication(argv)
UI = Main()
UI.show()
exit(APP.exec_())
