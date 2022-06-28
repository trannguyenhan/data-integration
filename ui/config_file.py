# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config_file.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConfigFile(object):
    def setupUi(self, ConfigFile):
        ConfigFile.setObjectName("ConfigFile")
        ConfigFile.resize(807, 509)
        self.browseFileButton = QtWidgets.QPushButton(ConfigFile)
        self.browseFileButton.setGeometry(QtCore.QRect(470, 50, 121, 31))
        self.browseFileButton.setObjectName("browseFileButton")
        self.tableSourceWidget = QtWidgets.QTableWidget(ConfigFile)
        self.tableSourceWidget.setEnabled(True)
        self.tableSourceWidget.setGeometry(QtCore.QRect(90, 140, 300, 261))
        self.tableSourceWidget.setTabletTracking(False)
        self.tableSourceWidget.setObjectName("tableSourceWidget")
        self.tableSourceWidget.setColumnCount(2)
        self.tableSourceWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableSourceWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSourceWidget.setHorizontalHeaderItem(1, item)
        self.tableDestWidget = QtWidgets.QTableWidget(ConfigFile)
        self.tableDestWidget.setGeometry(QtCore.QRect(440, 140, 300, 261))
        self.tableDestWidget.setObjectName("tableDestWidget")
        self.tableDestWidget.setColumnCount(2)
        self.tableDestWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableDestWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDestWidget.setHorizontalHeaderItem(1, item)
        self.previewButton = QtWidgets.QPushButton(ConfigFile)
        self.previewButton.setGeometry(QtCore.QRect(80, 460, 101, 25))
        self.previewButton.setObjectName("previewButton")
        self.okButton = QtWidgets.QPushButton(ConfigFile)
        self.okButton.setGeometry(QtCore.QRect(570, 460, 89, 25))
        self.okButton.setObjectName("okButton")
        self.removeBtn = QtWidgets.QPushButton(ConfigFile)
        self.removeBtn.setGeometry(QtCore.QRect(240, 410, 141, 25))
        self.removeBtn.setObjectName("removeBtn")
        self.btn_up = QtWidgets.QPushButton(ConfigFile)
        self.btn_up.setGeometry(QtCore.QRect(20, 220, 51, 41))
        self.btn_up.setObjectName("btn_up")
        self.btn_down = QtWidgets.QPushButton(ConfigFile)
        self.btn_down.setGeometry(QtCore.QRect(20, 280, 51, 41))
        self.btn_down.setObjectName("btn_down")
        self.label_4 = QtWidgets.QLabel(ConfigFile)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 81, 16))
        self.label_4.setObjectName("label_4")
        self.connectionLabel = QtWidgets.QLineEdit(ConfigFile)
        self.connectionLabel.setGeometry(QtCore.QRect(110, 50, 311, 31))
        self.connectionLabel.setObjectName("connectionLabel")
        self.loadBtn = QtWidgets.QPushButton(ConfigFile)
        self.loadBtn.setGeometry(QtCore.QRect(630, 50, 111, 31))
        self.loadBtn.setObjectName("loadBtn")

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
        self.removeBtn.setText(_translate("ConfigFile", "Remove Row"))
        self.btn_up.setText(_translate("ConfigFile", "Up"))
        self.btn_down.setText(_translate("ConfigFile", "Down"))
        self.label_4.setText(_translate("ConfigFile", "Connection"))
        self.loadBtn.setText(_translate("ConfigFile", "Connect/Load"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConfigFile = QtWidgets.QWidget()
    ui = Ui_ConfigFile()
    ui.setupUi(ConfigFile)
    ConfigFile.show()
    sys.exit(app.exec_())
