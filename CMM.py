# -*- coding: utf-8 -*-

from PyQt4.QtGui import QApplication
from ui.main import Main

if __name__ == "__main__":
    from sys import argv, exit
    app = QApplication(argv)
    ui = Main()
    ui.show()
    exit(app.exec_())
