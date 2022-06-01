# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/designs/init_project.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InitProject(object):
    def setupUi(self, InitProject):
        InitProject.setObjectName("InitProject")
        InitProject.resize(525, 374)
        self.label = QtWidgets.QLabel(InitProject)
        self.label.setGeometry(QtCore.QRect(20, 60, 71, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(InitProject)
        self.lineEdit.setGeometry(QtCore.QRect(100, 60, 331, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(InitProject)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 511, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(InitProject)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 61, 16))
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(InitProject)
        self.tableWidget.setGeometry(QtCore.QRect(100, 110, 411, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(59)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.testBtn = QtWidgets.QPushButton(InitProject)
        self.testBtn.setGeometry(QtCore.QRect(460, 60, 51, 28))
        self.testBtn.setObjectName("testBtn")
        self.nextBtn = QtWidgets.QPushButton(InitProject)
        self.nextBtn.setGeometry(QtCore.QRect(420, 330, 93, 28))
        self.nextBtn.setObjectName("nextBtn")
        self.addBtn = QtWidgets.QPushButton(InitProject)
        self.addBtn.setGeometry(QtCore.QRect(100, 330, 93, 28))
        self.addBtn.setObjectName("addBtn")
        self.removeBtn = QtWidgets.QPushButton(InitProject)
        self.removeBtn.setGeometry(QtCore.QRect(210, 330, 93, 28))
        self.removeBtn.setObjectName("removeBtn")

        self.retranslateUi(InitProject)
        QtCore.QMetaObject.connectSlotsByName(InitProject)

    def retranslateUi(self, InitProject):
        _translate = QtCore.QCoreApplication.translate
        InitProject.setWindowTitle(_translate("InitProject", "Project Initializaiton"))
        self.label.setText(_translate("InitProject", "Connection"))
        self.label_2.setText(_translate("InitProject", "Destination datasource setup"))
        self.label_3.setText(_translate("InitProject", "Schema"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("InitProject", "Column name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("InitProject", "Data type"))
        self.testBtn.setText(_translate("InitProject", "Test"))
        self.nextBtn.setText(_translate("InitProject", "Next"))
        self.addBtn.setText(_translate("InitProject", "Add"))
        self.removeBtn.setText(_translate("InitProject", "Remove"))

