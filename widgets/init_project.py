from PyQt5.QtWidgets import QWidget
from ui.init_project import Ui_InitProject
from PyQt5 import QtGui, QtWidgets
from dal.project_dao import set_is_initialized_to_true
from db import Database

class InitProject(QWidget):
    def __init__(self, navigator, project):
        super().__init__()
        self.navigator = navigator
        self.project = project
        self.uic = Ui_InitProject()
        self.uic.setupUi(self)
        self.uic.addBtn.clicked.connect(self.add)
        self.uic.removeBtn.clicked.connect(self.remove)
        self.uic.nextBtn.clicked.connect(self.next)
        self.uic.connectionLabel.setText(project[2])

    def add(self):
        '''
        Add a new row to the table
        '''
        rowcount = self.uic.tableWidget.rowCount()
        self.uic.tableWidget.setRowCount(rowcount + 1)
        cbx = QtWidgets.QComboBox()
        cbx.addItems(["string", "integer", "float", "date"])
        self.uic.tableWidget.setCellWidget(rowcount, 1, cbx)

    def remove(self):
        '''
        Remove a row of the table
        '''
        row = self.uic.tableWidget.currentRow()
        self.uic.tableWidget.removeRow(row)
    
    def next(self):
        # TODO: check valid
        set_is_initialized_to_true(self.project[0])
        self.create_table()
        self.hide()
        self.navigator.open_workbench()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.navigator.open_project_management_window()
        return super().closeEvent(a0)

    def create_table(self):
        # Get list of columns and their data type from the table
        columns = []
        for i in range(self.uic.tableWidget.rowCount()):
            column_name = self.uic.tableWidget.takeItem(i, 0).text()
            data_type = self.uic.tableWidget.cellWidget(i, 1).currentText()
            columns.append((column_name, data_type))
        
        # Create a new table to db
        project_name = self.project[1]
        Database.create_table(project_name, columns)