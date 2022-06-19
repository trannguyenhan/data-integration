import os
import re

import mysql
import mysql.connector
import pyodbc
from database import datasource_dao, project_dao
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem, QWidget
from ui.init_project import Ui_InitProject
from utils.constants import DataType, SourceType
from utils.context import Context


class InitProject(QWidget):
    def __init__(self, navigator, project):
        super().__init__()
        self.navigator = navigator
        self.project = project
        self.uic = Ui_InitProject()
        self.uic.setupUi(self)
        self.uic.testBtn.clicked.connect(self.test_connection)
        self.uic.addBtn.clicked.connect(self.add)
        self.uic.removeBtn.clicked.connect(self.remove)
        self.uic.nextBtn.clicked.connect(self.next)
        self.uic.browseBtn.clicked.connect(self.browse)
        if self.project["is initialized"]:
            self.uic.connectionLabel.setText(self.project["connection string"])
            self.load_schema_destination()
        else:
            # Set hint text
            dest_type = project["destination type"]
            if dest_type in [SourceType.TXT, SourceType.CSV, SourceType.XML, SourceType.JSON, SourceType.EXCEL]:
                hint = f"Path to destination {dest_type} file"
            elif dest_type == SourceType.MySQL:
                hint = "host=localhost; user=root; password=1234"
            elif dest_type == SourceType.MSSQL:
                hint = "SERVER=localhost;DATABASE=testdb;UID=sa;PWD=1234"
            else:
                raise Exception("Invalid destination type " + dest_type)
            self.uic.connectionLabel.setText(hint)

    def add(self,column_key="",type=DataType.OBJ):
        '''
        Add a new row to the table
        '''
        rowcount = self.uic.tableWidget.rowCount()
        self.uic.tableWidget.setRowCount(rowcount + 1)
        item = QTableWidgetItem()
        key = column_key if column_key else f"Column {rowcount}" 
        item.setText(key)
        self.uic.tableWidget.setItem(rowcount, 0, item)
        cbx = QtWidgets.QComboBox()
        cbx.addItems(DataType.ALL)
        cbx.setCurrentText(type)
        self.uic.tableWidget.setCellWidget(rowcount, 1, cbx)
    def load_schema_destination(self):
        if self.project["destination schema"] is None:
            return
        for column_key, type in self.project["destination schema"].items():
            print(type)
            self.add(column_key,type)

    def remove(self):
        '''
        Remove a row of the table
        '''
        row = self.uic.tableWidget.currentRow()
        self.uic.tableWidget.removeRow(row)
    
    def next(self):
        go_to_workbench = False
        if not self.project["is initialized"]:
            go_to_workbench = True
        if not self.check_connection():
            self.showError("Failed to connect to destination")
            return
        if self.uic.tableWidget.rowCount() == 0:
            self.showError("Columns list cannot be empty")
            return
        try:
            # Mark project is initialized
            project_dao.update_is_initialized(self.project["project name"], True)

            # Set connection string for project
            project_dao.set_connection_str(self.project["project name"], self.uic.connectionLabel.text())

            # Save project's destination schema
            is_schema_changed = self.save_destination_schema()

            # Open workbench
            self.hide()
            if go_to_workbench:
                self.navigator.open_workbench()
            if is_schema_changed:
                datasource_dao.reset_all_valid()
                self.navigator.workbench.update_input_source_status()
        except Exception as e:
            self.showError(str(e))

    def save_destination_schema(self):
        # Get list of columns and their data type from the table
        columns = {}
        for i in range(self.uic.tableWidget.rowCount()):
            column_name = self.uic.tableWidget.takeItem(i, 0).text()
            data_type = self.uic.tableWidget.cellWidget(i, 1).currentText()
            columns[column_name] = data_type
    
        #check change destination schema:
        is_schema_changed = columns != Context.project["destination schema"]
        # Save destination schema for project
        project_name = self.project["project name"]
        project_dao.set_destination_schema(project_name, columns)
        return is_schema_changed


    def test_connection(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Info")
        if self.check_connection():
            msg.setText("Test ok")
        else:
            msg.setText("Test fail")
        msg.show()

    def check_connection(self):
        dest_type = self.project['destination type']
        if dest_type in [SourceType.TXT, SourceType.CSV, SourceType.XML, SourceType.JSON, SourceType.EXCEL]:
            path = self.uic.connectionLabel.text()
            if not os.path.exists(path):
                return False
            if re.match('.*\.(csv|txt|xml|json|xls|xlsx)', path):
                return True
        elif dest_type == SourceType.MySQL:
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
        elif dest_type == SourceType.MSSQL:
            try:
                conn_str = self.uic.connectionLabel.text()
                host, database, user, password = conn_str.split(';')
                host = host.split("=")[1].strip()
                user = user.split("=")[1].strip()
                database = database.split("=")[1].strip()
                password = password.split("=")[1].strip()
                try:
                    con = pyodbc.connect(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={host};DATABASE={database};UID={user};PWD={password}")
                    con.close()
                    return True
                except Exception as e:
                    print(e)
                    return False
            except Exception as e:
                print("Connection string invalid")
                return False

    def browse(self):
        filename = QFileDialog.getOpenFileName()
        if len(filename) > 0:
            path = filename[0]
            self.uic.connectionLabel.setText(path)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        # self.navigator.open_project_management_window()
        return super().closeEvent(a0)

    def showError(self, str):
        msg = QMessageBox(self)
        msg.setWindowTitle("Error")
        msg.setText(str)
        msg.show()
