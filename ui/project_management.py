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
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout.addWidget(self.listWidget)
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
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("ProjectManagement", "Project 1"))
        item = self.listWidget.item(1)
        item.setText(_translate("ProjectManagement", "Project 2"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.open_btn.setText(_translate("ProjectManagement", "Open"))
        self.newproject_btn.setText(_translate("ProjectManagement", "New project"))

