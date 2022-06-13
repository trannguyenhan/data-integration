from database import datasource_dao, project_dao
from PyQt5 import QtWidgets
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QTableWidgetItem
from ui.config_file import Ui_ConfigFile
from utils import Context
from utils.constants import DataType


class ConfigFile(QMainWindow):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator
        self.uic = Ui_ConfigFile()
        self.uic.setupUi(self)
        self.uic.okButton.clicked.connect(self.ok_btn_clicked)
        self.uic.browseFileButton.clicked.connect(self.browse_file)
        self.uic.previewButton.clicked.connect(self.preview)
        self.uic.addBtn.clicked.connect(self.add)
        self.uic.removeBtn.clicked.connect(self.remove)
        self.uic.btn_up.clicked.connect(self.moveUp)
        self.uic.btn_down.clicked.connect(self.moveDown)

        self.create_components()

    def create_components(self):
        self.setWindowTitle(f"Config {Context.data_source['type']} data source")

        # Create source components
        rowcount = len(Context.data_source['schema'])
        self.uic.tableSourceWidget.setRowCount(rowcount)
        schema = Context.data_source['schema']
        for i, (col_name, col_dtype) in enumerate(schema.items()):
            cbx = QtWidgets.QComboBox()
            cbx.addItems(DataType.ALL)
            cbx.setCurrentIndex(DataType.ALL.index(col_dtype))
            item = QTableWidgetItem()
            item.setText(col_name)
            self.uic.tableSourceWidget.setItem(i, 0, item)
            self.uic.tableSourceWidget.setCellWidget(i, 1, cbx)

        # TODO: create dest components


    def add(self):
        '''
        Add a new row to the table
        '''
        rowcount = self.uic.tableSourceWidget.rowCount()
        self.uic.tableSourceWidget.setRowCount(rowcount + 1)
        item = QTableWidgetItem()
        item.setText(f"Column {rowcount}")
        self.uic.tableSourceWidget.setItem(rowcount, 0, item)
        cbx = QtWidgets.QComboBox()
        cbx.addItems(DataType.ALL)
        self.uic.tableSourceWidget.setCellWidget(rowcount, 1, cbx)

    def remove(self):
        '''
        Remove a row of the table
        '''
        row = self.uic.tableSourceWidget.currentRow()
        self.uic.tableSourceWidget.removeRow(row)

    def ok_btn_clicked(self):
        self.navigator.config_file.hide()

        # Save schema
        schema = {}
        for i in range(self.uic.tableSourceWidget.rowCount()):
            col_name = self.uic.tableSourceWidget.takeItem(i, 0).text()
            col_dtype = self.uic.tableSourceWidget.cellWidget(i, 1).currentText()
            schema[col_name] = col_dtype
        Context.data_source['schema'] = schema
        datasource_dao.save()

    def browse_file(self):
        filename = QFileDialog.getOpenFileName()
        try:
            path = filename[0]
            with open(path, "r") as f:
                print(f.readline())
        except Exception as e:
            print(str(e))

    def preview(self):
        self.navigator.open_preview()
    def moveDown(self):
        row = self.uic.tableSourceWidget.currentRow()
        column = self.uic.tableSourceWidget.currentColumn();
        if row < self.uic.tableSourceWidget.rowCount()-1:
            self.uic.tableSourceWidget.insertRow(row+2)
            for i in range(self.uic.tableSourceWidget.columnCount()):
               self.uic.tableSourceWidget.setItem(row+2,i,self.uic.tableSourceWidget.takeItem(row,i))
               self.uic.tableSourceWidget.setCurrentCell(row+2,column)
            self.uic.tableSourceWidget.removeRow(row)        


    def moveUp(self):    
        row = self.uic.tableSourceWidget.currentRow()
        column = self.uic.tableSourceWidget.currentColumn();
        if row > 0:
            self.uic.tableSourceWidget.insertRow(row-1)
            for i in range(self.uic.tableSourceWidget.columnCount()):
               self.uic.tableSourceWidget.setItem(row-1,i,self.uic.tableSourceWidget.takeItem(row+1,i))
               self.uic.tableSourceWidget.setCurrentCell(row-1,column)
            self.uic.tableSourceWidget.removeRow(row+1)   
