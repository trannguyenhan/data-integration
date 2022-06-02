from PyQt5.QtWidgets import QWidget, QMessageBox
from ui.init_project import Ui_InitProject
from PyQt5 import QtGui, QtWidgets
from dal.project_dao import set_is_initialized_to_true, set_connection_str
from dal.utils_dao import create_table
from db import Database
import os
import re
import pyodbc
import mysql
import mysql.connector

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

        # Set hint text
        dest_type = project[2]
        if dest_type in ["Flatfile", "Xml", "Json", "Excel"]:
            hint = f"Path to destination {dest_type} file"
        elif dest_type == "MySQL":
            hint = "host=localhost; user=root; password=1234"
        else:
            hint = "SERVER=localhost;DATABASE=testdb;UID=sa;PWD=1234"
        self.uic.connectionLabel.setText(hint)

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
        if not self.check_connection():
            msg = QMessageBox(self)
            msg.setWindowTitle("Info")
            msg.setText("Failed to connect to destination")
            msg.show()
            return
        if self.uic.tableWidget.rowCount() == 0:
            msg = QMessageBox(self)
            msg.setWindowTitle("Error")
            msg.setText("Columns list cannot be empty")
            msg.show()
            return
        set_is_initialized_to_true(self.project[0])
        set_connection_str(self.project[0], self.uic.connectionLabel.text())
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
        create_table(project_name, columns)

    def test_connection(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Info")
        if self.check_connection():
            msg.setText("Test ok")
        else:
            msg.setText("Test fail")
        msg.show()

    def check_connection(self):
        dest_type = self.project[2]
        if dest_type in ["Flatfile", "Xml", "Json", "Excel"]:
            path = self.uic.connectionLabel.text()
            if not os.path.exists(path):
                return False
            if re.match('.*\.(csv|txt)', path):
                return True
        elif dest_type == "MySQL":
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
        elif dest_type == "SQL Server":
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