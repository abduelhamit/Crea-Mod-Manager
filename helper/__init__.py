#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import QProcess


def process_command(q_parent, command):
    process = QProcess(q_parent)
    process.start(command)
    process.waitForFinished()
    return process.readAllStandardOutput().data()
