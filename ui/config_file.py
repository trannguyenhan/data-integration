# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/designs/config_file.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConfigFile(object):
    def setupUi(self, ConfigFile):
        ConfigFile.setObjectName("ConfigFile")
        ConfigFile.resize(739, 509)
        self.browseFileButton = QtWidgets.QPushButton(ConfigFile)
        self.browseFileButton.setGeometry(QtCore.QRect(60, 50, 291, 41))
        self.browseFileButton.setObjectName("browseFileButton")
        self.tableSourceWidget = QtWidgets.QTableWidget(ConfigFile)
        self.tableSourceWidget.setEnabled(True)
        self.tableSourceWidget.setGeometry(QtCore.QRect(80, 140, 251, 261))
        self.tableSourceWidget.setTabletTracking(False)
        self.tableSourceWidget.setObjectName("tableSourceWidget")
        self.tableSourceWidget.setColumnCount(2)
        self.tableSourceWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableSourceWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSourceWidget.setHorizontalHeaderItem(1, item)
        self.tableDestWidget = QtWidgets.QTableWidget(ConfigFile)
        self.tableDestWidget.setGeometry(QtCore.QRect(440, 140, 261, 261))
        self.tableDestWidget.setObjectName("tableDestWidget")
        self.tableDestWidget.setColumnCount(2)
        self.tableDestWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableDestWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDestWidget.setHorizontalHeaderItem(1, item)
        self.previewButton = QtWidgets.QPushButton(ConfigFile)
        self.previewButton.setGeometry(QtCore.QRect(80, 460, 89, 25))
        self.previewButton.setObjectName("previewButton")
        self.okButton = QtWidgets.QPushButton(ConfigFile)
        self.okButton.setGeometry(QtCore.QRect(610, 460, 89, 25))
        self.okButton.setObjectName("okButton")
        self.addBtn = QtWidgets.QPushButton(ConfigFile)
        self.addBtn.setGeometry(QtCore.QRect(80, 410, 89, 25))
        self.addBtn.setObjectName("addBtn")
        self.removeBtn = QtWidgets.QPushButton(ConfigFile)
        self.removeBtn.setGeometry(QtCore.QRect(250, 410, 89, 25))
        self.removeBtn.setObjectName("removeBtn")

        self.retranslateUi(ConfigFile)
        QtCore.QMetaObject.connectSlotsByName(ConfigFile)

    def retranslateUi(self, ConfigFile):
        _translate = QtCore.QCoreApplication.translate
        ConfigFile.setWindowTitle(_translate("ConfigFile", "Config Source File"))
        self.browseFileButton.setText(_translate("ConfigFile", "Browse file"))
        item = self.tableSourceWidget.horizontalHeaderItem(0)
        item.setText(_translate("ConfigFile", "Column Name"))
        item = self.tableSourceWidget.horizontalHeaderItem(1)
        item.setText(_translate("ConfigFile", "Data Type"))
        item = self.tableDestWidget.horizontalHeaderItem(0)
        item.setText(_translate("ConfigFile", "Column Name"))
        item = self.tableDestWidget.horizontalHeaderItem(1)
        item.setText(_translate("ConfigFile", "Data Type"))
        self.previewButton.setText(_translate("ConfigFile", "Preview"))
        self.okButton.setText(_translate("ConfigFile", "OK"))
        self.addBtn.setText(_translate("ConfigFile", "Add"))
        self.removeBtn.setText(_translate("ConfigFile", "Remove"))

