# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/designs/new_project.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewProject(object):
    def setupUi(self, NewProject):
        NewProject.setObjectName("NewProject")
        NewProject.resize(400, 283)
        self.label = QtWidgets.QLabel(NewProject)
        self.label.setGeometry(QtCore.QRect(30, 40, 81, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(NewProject)
        self.lineEdit.setGeometry(QtCore.QRect(130, 40, 251, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.okBtn = QtWidgets.QPushButton(NewProject)
        self.okBtn.setGeometry(QtCore.QRect(160, 240, 93, 28))
        self.okBtn.setObjectName("okBtn")
        self.label_2 = QtWidgets.QLabel(NewProject)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 81, 16))
        self.label_2.setObjectName("label_2")
        self.destinationCbx = QtWidgets.QComboBox(NewProject)
        self.destinationCbx.setGeometry(QtCore.QRect(130, 80, 251, 22))
        self.destinationCbx.setObjectName("destinationCbx")
        self.destinationCbx.addItem("")
        self.destinationCbx.addItem("")
        self.destinationCbx.addItem("")
        self.destinationCbx.addItem("")
        self.destinationCbx.addItem("")
        self.destinationCbx.addItem("")

        self.retranslateUi(NewProject)
        QtCore.QMetaObject.connectSlotsByName(NewProject)

    def retranslateUi(self, NewProject):
        _translate = QtCore.QCoreApplication.translate
        NewProject.setWindowTitle(_translate("NewProject", "New Project"))
        self.label.setText(_translate("NewProject", "Project name"))
        self.okBtn.setText(_translate("NewProject", "OK"))
        self.label_2.setText(_translate("NewProject", "Destination"))
        self.destinationCbx.setItemText(0, _translate("NewProject", "Flatfile"))
        self.destinationCbx.setItemText(1, _translate("NewProject", "Excel"))
        self.destinationCbx.setItemText(2, _translate("NewProject", "Xml"))
        self.destinationCbx.setItemText(3, _translate("NewProject", "Json"))
        self.destinationCbx.setItemText(4, _translate("NewProject", "SQL Server"))
        self.destinationCbx.setItemText(5, _translate("NewProject", "MySQL"))

