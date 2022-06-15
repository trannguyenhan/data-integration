import os
import re
import mysql
import mysql.connector
import pyodbc
from engine1.engine_csv import EngineCsv
from engine1.engine_json import EngineJson
from engine1.engine_xml import EngineXml
from database import datasource_dao
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QTableWidgetItem, QMessageBox
from ui.config_file import Ui_ConfigFile
from utils import Context
from utils.constants import DataType, SourceType


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
        self.uic.btn_up.clicked.connect(self.move_up)
        self.uic.btn_down.clicked.connect(self.move_down)
        self.uic.loadBtn.clicked.connect(self.load_source_file)

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
        if len(filename) > 0:
            path = filename[0]
            self.uic.connectionLabel.setText(path)

    def load_source_file(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Info")
        if self.check_connection():
            path = self.uic.connectionLabel.text()
            msg.setText("Success")
            file_to_load = [
                [SourceType.JSON, 'json', EngineJson(self.uic.connectionLabel.text())],
                [SourceType.CSV, 'csv', EngineCsv(self.uic.connectionLabel.text())],
                [SourceType.XML, 'xml', EngineXml(self.uic.connectionLabel.text())],
            ]
            for file in file_to_load:
                if check_file_is_valid(file[0], file[1], path, msg, file[2]):
                    engine = file[2]
                    self.load_schema_to_source_table(engine)
        else:
            msg.setText("Load file fail")
        msg.show()

    def load_schema_to_source_table(self, engine):
        datas = engine.extract_schema()
        while self.uic.tableSourceWidget.rowCount() > 0:
            self.uic.tableSourceWidget.removeRow(0)
        row = 0
        self.uic.tableSourceWidget.setRowCount(len(datas))
        for key in datas:
            item = QTableWidgetItem()
            item.setText(key)
            cbx = QtWidgets.QComboBox()
            cbx.addItems(DataType.ALL)
            cbx.setCurrentIndex(DataType.ALL.index(datas[key]))
            self.uic.tableSourceWidget.setItem(row, 0, item)
            self.uic.tableSourceWidget.setCellWidget(row, 1, cbx)
            row = row + 1

    def check_connection(self):
        if Context.data_source['type'] in [SourceType.TXT, SourceType.CSV, SourceType.XML, SourceType.JSON,
                                           SourceType.EXCEL]:
            path = self.uic.connectionLabel.text()
            if not os.path.exists(path):
                return False
            if re.match('.*\.(csv|txt|xml|json|xls|xlsx)', path):
                return True
        elif Context.data_source['type'] == SourceType.MySQL:
            try:
                conn_str = self.uic.connectionLabel.text()
                host, user, password = conn_str.split(';')
                host = host.split("=")[1].strip()
                user = user.split("=")[1].strip()
                password = password.split("=")[1].strip()
                try:
                    con = mysql.connector.connect(host=host, user=user, password=password)
                    con.disconnect()
                    return True
                except Exception as e:
                    print(e)
                    return False
            except Exception as e:
                print("Connection string invalid")
                return False
        elif Context.data_source['type'] == SourceType.MSSQL:
            try:
                conn_str = self.uic.connectionLabel.text()
                host, database, user, password = conn_str.split(';')
                host = host.split("=")[1].strip()
                user = user.split("=")[1].strip()
                database = database.split("=")[1].strip()
                password = password.split("=")[1].strip()
                try:
                    con = pyodbc.connect(
                        f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={host};DATABASE={database};UID={user};PWD={password}")
                    con.close()
                    return True
                except Exception as e:
                    print(e)
                    return False
            except Exception as e:
                print("Connection string invalid")
                return False

    def preview(self):
        self.navigator.open_preview()

    def move_down(self):
        row = self.uic.tableSourceWidget.currentRow()
        column = self.uic.tableSourceWidget.currentColumn();
        if row < self.uic.tableSourceWidget.rowCount() - 1:
            self.uic.tableSourceWidget.insertRow(row + 2)
            self.uic.tableSourceWidget.setItem(row + 2, 0, self.uic.tableSourceWidget.takeItem(row, 0))
            self.uic.tableSourceWidget.setCellWidget(row + 2, 1, self.uic.tableSourceWidget.cellWidget(row, 1))
            self.uic.tableSourceWidget.setCurrentCell(row + 2, column)
            self.uic.tableSourceWidget.removeRow(row)

    def move_up(self):
        row = self.uic.tableSourceWidget.currentRow()
        column = self.uic.tableSourceWidget.currentColumn();
        if row > 0:
            self.uic.tableSourceWidget.insertRow(row - 1)
            self.uic.tableSourceWidget.setItem(row - 1, 0, self.uic.tableSourceWidget.takeItem(row + 1, 0))
            self.uic.tableSourceWidget.setCellWidget(row - 1, 1, self.uic.tableSourceWidget.cellWidget(row + 1, 1))
            self.uic.tableSourceWidget.setCurrentCell(row - 1, column)
            self.uic.tableSourceWidget.removeRow(row + 1)


def check_file_is_valid(file_type, file_extension, path, msg, engine_type):
    source_type = Context.data_source['type']
    if source_type == file_type:
        if not re.match(f'.*\.{file_extension}', path):
            msg.setText(f"Not a {file_extension} file")
            return False
        else:
            return True
