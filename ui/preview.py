# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preview.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Preview(object):
    def setupUi(self, Preview):
        Preview.setObjectName("Preview")
        Preview.resize(888, 558)
        self.tableWidget = QtWidgets.QTableWidget(Preview)
        self.tableWidget.setGeometry(QtCore.QRect(40, 40, 810, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.okButton = QtWidgets.QPushButton(Preview)
        self.okButton.setGeometry(QtCore.QRect(380, 470, 151, 41))
        self.okButton.setObjectName("okButton")

        self.retranslateUi(Preview)
        QtCore.QMetaObject.connectSlotsByName(Preview)

    def retranslateUi(self, Preview):
        _translate = QtCore.QCoreApplication.translate
        Preview.setWindowTitle(_translate("Preview", "Preview"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Preview", "Row1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Preview", "Row2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Preview", "Row3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Preview", "Row4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Preview", "Row5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Preview", "Row6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Preview", "Row7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Preview", "Row8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Preview", "Row9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Preview", "Row10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Preview", "Column1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Preview", "Column2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Preview", "Column3"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Preview", "Column4"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Preview", "Column5"))
        self.okButton.setText(_translate("Preview", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Preview = QtWidgets.QWidget()
    ui = Ui_Preview()
    ui.setupUi(Preview)
    Preview.show()
    sys.exit(app.exec_())
