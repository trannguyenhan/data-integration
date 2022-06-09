# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/designs/project_management.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProjectManagement(object):
    def setupUi(self, ProjectManagement):
        ProjectManagement.setObjectName("ProjectManagement")
        ProjectManagement.resize(463, 319)
        ProjectManagement.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(ProjectManagement)
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 549))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.open_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_btn.setObjectName("open_btn")
        self.horizontalLayout.addWidget(self.open_btn)
        self.newproject_btn = QtWidgets.QPushButton(self.centralwidget)
        self.newproject_btn.setObjectName("newproject_btn")
        self.horizontalLayout.addWidget(self.newproject_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        ProjectManagement.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ProjectManagement)
        self.statusbar.setObjectName("statusbar")
        ProjectManagement.setStatusBar(self.statusbar)

        self.retranslateUi(ProjectManagement)
        QtCore.QMetaObject.connectSlotsByName(ProjectManagement)

    def retranslateUi(self, ProjectManagement):
        _translate = QtCore.QCoreApplication.translate
        ProjectManagement.setWindowTitle(_translate("ProjectManagement", "Project Mangement"))
        self.label.setText(_translate("ProjectManagement", "Project list"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ProjectManagement", "Project Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ProjectManagement", "Destination type"))
        self.open_btn.setText(_translate("ProjectManagement", "Open"))
        self.newproject_btn.setText(_translate("ProjectManagement", "New project"))

