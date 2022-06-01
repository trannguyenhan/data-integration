from PyQt5.QtWidgets import QWidget
from ui.init_project import Ui_InitProject
from PyQt5 import QtGui, QtWidgets

class InitProject(QWidget):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator
        self.uic = Ui_InitProject()
        self.uic.setupUi(self)
        self.uic.addBtn.clicked.connect(self.add)
        self.uic.removeBtn.clicked.connect(self.remove)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.navigator.open_project_management_window()
        return super().closeEvent(a0)

    def add(self):
        rowcount = self.uic.tableWidget.rowCount()
        self.uic.tableWidget.setRowCount(rowcount + 1)

    def remove(self):
        row = self.uic.tableWidget.currentRow()
        self.uic.tableWidget.removeRow(row)
        