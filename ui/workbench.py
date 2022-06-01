# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/designs/workbench.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_workbench(object):
    def setupUi(self, workbench):
        workbench.setObjectName("workbench")
        workbench.resize(400, 300)

        self.retranslateUi(workbench)
        QtCore.QMetaObject.connectSlotsByName(workbench)

    def retranslateUi(self, workbench):
        _translate = QtCore.QCoreApplication.translate
        workbench.setWindowTitle(_translate("workbench", "Workbench"))

