from threading import Timer

from database import datasource_dao
from my_engine import *
from my_engine import EngineCsv, EngineJson, EngineMysql, EngineXml
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, QEvent, Qt
from PyQt5.QtGui import QCloseEvent, QIcon, QMovie, QPainter
from PyQt5.QtWidgets import (QErrorMessage, QInputDialog, QMainWindow,
                             QMessageBox, QPushButton, QWidget)
from ui.workbench import Ui_Workbench
from utils.constants import DataType, SourceType
from utils.context import Context
from utils.helpers import get_mysql_connection
from utils.warehouse import dump_with_engine


def setTimeout(fn, ms, *args, **kwargs): 
    t = Timer(ms / 1000., fn, args=args, kwargs=kwargs) 
    t.start() 
    return t 

class Workbench(QWidget):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator
        self.uic = Ui_Workbench()
        self.uic.setupUi(self)
        self.setup_menu_type()
        self.uic.btn_back.clicked.connect(self.back)
        self.uic.btn_destination.clicked.connect(self.des_btn_clicked) 
        self.uic.btn_run.clicked.connect(self.run_btn_click) 
        self.loading = QMovie("././assets/loading.gif")
        self.uic.loading_label.setMovie(self.loading)
        self.uic.loading_label.setHidden(True)
        self.dict_engine ={
            SourceType.XML:  EngineXml,
            SourceType.JSON: EngineJson,
            SourceType.CSV: EngineCsv,
        }
        self.loading.start()
        self.create_components()

    def create_components(self):
        '''Read project's info and create corresponding components'''
        self.setWindowTitle(
            f"Project \'{Context.project['project name']}\' - Workbench")
        # Loading the GIF

        for input_source in Context.project["data sources"]:
            self.add_input_source_btn(input_source)

    def setup_menu_type(self):
        '''Setup a popup menu to choose source data type'''
        menu = QtWidgets.QMenu()
        menu.triggered.connect(self.menu_item_clicked)
        self.uic.btn_add.setMenu(menu)
        for type in SourceType.ALL:
            action = menu.addAction(type)
            action.setIconVisibleInMenu(False)

    def menu_item_clicked(self, item):
        datasource_dao.add(item.text())
        self.add_input_source_btn(Context.project['data sources'][-1])

    def end_process(self):
        self.uic.loading_label.setHidden(True)
        self.uic.btn_run.setEnabled(True)
    
    def run_btn_click(self):        
        for input_source in Context.project["data sources"]:
            if not input_source["is valid"]:
                QErrorMessage(self).showMessage("Input source config is invalid!")
                return
        
        self.uic.loading_label.setHidden(False)
        self.uic.btn_run.setEnabled(False)

        lst = []
        for input_source in Context.project["data sources"]:
            if (input_source["type"] in self.dict_engine):
                engine = self.dict_engine[input_source["type"]]
                lst.append({
                    "engine": engine(input_source["connection string"]),
                    "mapping_target": input_source["mapping"]
                })
            elif input_source["type"] == SourceType.TXT:
                engine = EngineCsv(
                    input_source["connection string"], 
                    delimiter="\t", 
                ) 
                lst.append({
                    "engine": engine,
                    "mapping_target": input_source["mapping"]
                })
            elif input_source["type"] == SourceType.EXCEL:
                engine = EngineCsv(
                    input_source["connection string"], 
                    delimiter=",", 
                    type_file=SourceType.EXCEL
                ) 
                lst.append({
                    "engine": engine,
                    "mapping_target": input_source["mapping"]
                })
            elif input_source["type"] == SourceType.MySQL:
                host, user, password, database, table_name = get_mysql_connection(input_source["connection string"])
                engine = EngineMysql(host,user,password,database,table_name ) 
                lst.append({
                    "engine": engine,
                    "mapping_target": input_source["mapping"]
                })
                
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Duplicate Check!")
        dlg.setText("Do you want to automatically remove duplicate?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()

        if button == QMessageBox.Yes:
            dump_with_engine(lst,Context.project["project name"],Context.project["destination type"], True)
        else:
            dump_with_engine(lst,Context.project["project name"],Context.project["destination type"], False)

        # setTimeout(self.end_process,2500)

        self.end_process()
        QErrorMessage(self).showMessage("Success!")

    def src_btn_clicked(self):
        idx = self.uic.verticalLayout.indexOf(self.sender())
        input_src = Context.project["data sources"][idx]
        Context.data_source = input_src 
        self.navigator.open_config_file()
    def des_btn_clicked(self):
        self.navigator.open_init_project_window()

    def add_input_source_btn(self, input_source):
        # Create input source button
        btn_source = QtWidgets.QPushButton(
            self.uic.scrollAreaWidgetContents)
        btn_source.setText(input_source["type"])
        count = self.uic.verticalLayout.count()
        self.uic.verticalLayout.insertWidget(count - 1, btn_source)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        btn_source.setSizePolicy(sizePolicy)
        btn_source.setMaximumSize(QtCore.QSize(16777215, 135))
        btn_source.clicked.connect(self.src_btn_clicked)
        btn_source.setIcon(QIcon('././assets/icons-green.png') if input_source["is valid"] else QIcon('././assets/icons-warning.png'))
        btn_source.installEventFilter(self)

    def back(self):
        self.hide()
        self.navigator.open_project_management_window()

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.navigator.open_project_management_window()
        return super().closeEvent(a0)

    def eventFilter(self, o, e):
        if e.type() == QEvent.Move:
            self.update()
        elif e.type() == QEvent.MouseButtonPress:
            if e.button() == Qt.RightButton:
                self.delete_input_source(o)
        return super().eventFilter(o, e)

    def delete_input_source(self, btn):
        idx = self.uic.verticalLayout.indexOf(btn)
        datasource_dao.remove_at(idx)
        self.uic.verticalLayout.removeWidget(btn)
        btn.deleteLater()
    def update_input_source_status(self):
        for indx,input_source in enumerate(Context.project["data sources"]):
            self.uic.verticalLayout.itemAt(indx).widget().setIcon(QIcon('././assets/icons-green.png') if input_source["is valid"] else QIcon('././assets/icons-warning.png'))
    def paintEvent(self, event):
        painter = QPainter(self)
        btn_des = self.uic.btn_destination.geometry()
        x_des = btn_des.x()
        y_des = btn_des.y() + btn_des.height()/2
        count = self.uic.verticalLayout.count() - 1
        for i in range(count):
            btn = self.uic.verticalLayout.itemAt(i)
            btn_source_geo = btn.geometry()
            x_source = btn_source_geo.x() + btn_source_geo.width()
            y_source = btn_source_geo.y() + btn_source_geo.height()
            painter.drawLine(x_source, y_source, x_des, y_des)
