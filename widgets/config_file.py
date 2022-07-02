import json

from database import datasource_dao
from my_engine import (EngineCsv, EngineJson, EngineMssql, EngineMysql,
                       EngineXml)
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QErrorMessage, QFileDialog, QMainWindow,
                             QMessageBox, QTableWidgetItem)
from sqlalchemy import true
from ui.config_file import Ui_ConfigFile
from utils.constants import DataType, SourceType
from utils.context import Context
from utils.helpers import check_connection, get_db_connection


class ConfigFile(QMainWindow):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator
        self.uic = Ui_ConfigFile()
        self.uic.setupUi(self)
        self.uic.okButton.clicked.connect(self.ok_btn_clicked)
        self.uic.browseFileButton.clicked.connect(self.browse_file)
        self.uic.previewButton.clicked.connect(self.open_preview)
        self.uic.removeBtn.clicked.connect(self.remove)
        self.uic.btn_up.clicked.connect(self.move_up)
        self.uic.btn_down.clicked.connect(self.move_down)
        self.uic.loadBtn.clicked.connect(self.load_source_file)

        self.create_components()

    def create_components(self):
        self.setWindowTitle(f"Config {Context.data_source['type']} data source")

        # Setup and display connection string
        if Context.data_source["connection string"] != "":
            self.uic.connectionLabel.setText(Context.data_source["connection string"])
        else:
            data_source_type = Context.data_source['type']
            if data_source_type in SourceType.FILE:
                hint = f"Path to destination {data_source_type} file"
            elif data_source_type == SourceType.MySQL:
                hint = "host=localhost; user=root; password=1234; database=testdb; table_name=test_table"
            elif data_source_type == SourceType.MSSQL:
                hint = "SERVER=localhost;UID=sa;PWD=1234;DATABASE=testdb;TABLE=test_table"
            else:
                raise Exception("Invalid destination type " + data_source_type)
            self.uic.connectionLabel.setText(hint)

        # Load source table
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

        # Load dest table
        self.uic.tableDestWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for column_key, type in Context.project["destination schema"].items():
            rowcount = self.uic.tableDestWidget.rowCount()
            self.uic.tableDestWidget.setRowCount(rowcount + 1)
            item = QTableWidgetItem()
            item.setText(column_key)
            data_type = QTableWidgetItem()
            data_type.setText(type)
            self.uic.tableDestWidget.setItem(rowcount, 0, item)
            self.uic.tableDestWidget.setItem(rowcount, 1, data_type)

    def remove(self):
        '''
        Remove a row of the table
        '''
        row = self.uic.tableSourceWidget.currentRow()
        self.uic.tableSourceWidget.removeRow(row)

    def mapping_schemas(self):
        if self.uic.tableSourceWidget.rowCount() != self.uic.tableDestWidget.rowCount() or self.uic.tableSourceWidget.rowCount() <= 0:
            return False, "Unequal number of columns!"
        mapping_dict = {}    
        for i in range(self.uic.tableSourceWidget.rowCount()):
            s_col_name = self.uic.tableSourceWidget.item(i, 0).text()
            s_col_dtype = self.uic.tableSourceWidget.cellWidget(i, 1).currentText()
            d_col_name = self.uic.tableDestWidget.item(i, 0).text()
            d_col_dtype = self.uic.tableDestWidget.item(i, 1).text()
            if s_col_dtype != d_col_dtype:
                return False, "Data type cannot mapping from column " + s_col_name + " to column " + d_col_name
            mapping_dict[s_col_name]=d_col_name
        return True, mapping_dict

    def ok_btn_clicked(self):
        can_map, data_map = self.mapping_schemas()
        if not can_map:
            QErrorMessage(self).showMessage(data_map)
            return

        self.navigator.config_file.hide()
        # Save schema
        schema = {}
        for i in range(self.uic.tableSourceWidget.rowCount()):
            col_name = self.uic.tableSourceWidget.takeItem(i, 0).text()
            col_dtype = self.uic.tableSourceWidget.cellWidget(i, 1).currentText()
            schema[col_name] = col_dtype
        Context.data_source['schema'] = schema
        Context.data_source['is valid'] = True
        Context.data_source['connection string']  = self.uic.connectionLabel.text()
        Context.data_source['mapping'] = data_map

        datasource_dao.save()
        self.navigator.workbench.update_input_source_status()

    def browse_file(self):
        filename = QFileDialog.getOpenFileName()
        if len(filename) > 0:
            path = filename[0]
            self.uic.connectionLabel.setText(path)

    def load_source_file(self):
        path = self.uic.connectionLabel.text()
        input_src_type = Context.data_source['type']
        check, message = check_connection(input_src_type,path)
        if not check:
            QErrorMessage(self).showMessage(message)
            return
        try:
            if input_src_type == SourceType.TXT:
                engine = EngineCsv(self.uic.connectionLabel.text(),  delimiter="\t")
            elif input_src_type == SourceType.CSV:
                engine = EngineCsv(self.uic.connectionLabel.text())
            elif input_src_type == SourceType.XML:
                engine = EngineXml(self.uic.connectionLabel.text())
            elif input_src_type == SourceType.JSON:
                engine = EngineJson(self.uic.connectionLabel.text())
            elif input_src_type ==  SourceType.EXCEL:
                engine = EngineCsv(self.uic.connectionLabel.text(), delimiter="," , type_file=SourceType.EXCEL)
            elif input_src_type == SourceType.MySQL:
                host, user, password, database, table_name = get_db_connection(path)
                engine = EngineMysql(host, user, password, database, table_name)
            elif input_src_type == SourceType.MSSQL:
                host, user, password, database, table_name = get_db_connection(path)
                engine = EngineMssql(host, user, password, database, table_name)
            self.load_schema_to_source_table(engine)
        except Exception as e:
            QErrorMessage(self).showMessage(f"Error when loading: {str(e)}")

    def load_schema_to_source_table(self, engine):
        keys = engine.extract_header()
        Context.data_source['keys'] = keys[:]
        sample_datas = engine.get_sample_data()
        Context.data_source['sample_datas'] = json.dumps(sample_datas,default=str) 
        datas = engine.extract_schema_v2()
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

    def open_preview(self):
        self.navigator.open_preview(Context.data_source['keys'], json.loads(Context.data_source['sample_datas']))

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
