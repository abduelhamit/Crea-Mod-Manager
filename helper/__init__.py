#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import QProcess


def process_command(command):
    process = QProcess()
    process.start(command)
    process.waitForFinished()
    return process.readAllStandardOutput().data()
