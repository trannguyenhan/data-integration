# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\designs\new_project.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewProject(object):
    def setupUi(self, NewProject):
        NewProject.setObjectName("NewProject")
        NewProject.resize(400, 300)
        self.label = QtWidgets.QLabel(NewProject)
        self.label.setGeometry(QtCore.QRect(30, 40, 81, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(NewProject)
        self.lineEdit.setGeometry(QtCore.QRect(130, 40, 251, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(NewProject)
        self.pushButton.setGeometry(QtCore.QRect(160, 250, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(NewProject)
        QtCore.QMetaObject.connectSlotsByName(NewProject)

    def retranslateUi(self, NewProject):
        _translate = QtCore.QCoreApplication.translate
        NewProject.setWindowTitle(_translate("NewProject", "New Project"))
        self.label.setText(_translate("NewProject", "Project name"))
        self.pushButton.setText(_translate("NewProject", "OK"))

