from database import datasource_dao
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, QEvent, Qt
from PyQt5.QtGui import QCloseEvent, QPainter
from PyQt5.QtWidgets import QMainWindow, QWidget
from ui.workbench import Ui_Workbench
from utils import Context
from utils.constants import SourceType


class Workbench(QWidget):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator
        self.uic = Ui_Workbench()
        self.uic.setupUi(self)
        self.setup_menu_type()
        self.uic.btn_back.clicked.connect(self.back)
        self.uic.btn_destination.clicked.connect(self.des_btn_clicked) 
        self.create_components()

    def create_components(self):
        '''Read project's info and create corresponding components'''
        self.setWindowTitle(
            f"Project \'{Context.project['project name']}\' - Workbench")

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
