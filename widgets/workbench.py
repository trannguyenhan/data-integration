from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, QEvent
from PyQt5.QtGui import QCloseEvent, QPainter
from PyQt5.QtWidgets import QMainWindow, QWidget
from ui.workbench import Ui_Workbench
from utils.constants import SourceType
from utils import Context
from database import datasource_dao


class Workbench(QWidget):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator
        self.uic = Ui_Workbench()
        self.list_input_source = []
        self.type_inputs = SourceType.ALL
        self.uic.setupUi(self)
        self.uic.list_btn_source = []
        self.setup_menu_type()
        self.uic.btn_back.clicked.connect(self.back)
        self.uic.btn_run.clicked.connect(self.remove_input_source)
        self.load()

    def load(self):
        self.setWindowTitle(f"Project \'{Context.project['project name']}\' - Workbench")

        for dsource in Context.project["data sources"]:
            self.add_input_source(dsource["type"])

    def setup_menu_type(self):
        '''Setup a popup menu to choose source data type'''
        menu = QtWidgets.QMenu()
        menu.triggered.connect(self.menu_item_clicked)
        self.uic.btn_add.setMenu(menu)
        for type in self.type_inputs:
            action = menu.addAction(type)
            action.setIconVisibleInMenu(False)

    def menu_item_clicked(self, item):
        self.add_input_source(item.text())
        datasource_dao.add(item.text())

    def add_input_source(self, type):
        self.list_input_source.append(type)
        self.uic.list_btn_source.append(self.create_btn(type))

    def remove_input_source(self, idx=5):
        if not self.list_input_source:
            return
        self.list_input_source.pop(idx)
        btn = self.uic.list_btn_source.pop(idx)
        btn.deleteLater()

    def create_btn(self, text):
        btn_source = QtWidgets.QPushButton(self.uic.scrollAreaWidgetContents)
        btn_source.setText(text)
        count = self.uic.verticalLayout.count()
        self.uic.verticalLayout.insertWidget(count - 1, btn_source)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        btn_source.setSizePolicy(sizePolicy)
        btn_source.setMaximumSize(QtCore.QSize(16777215, 135))
        btn_source.clicked.connect(self.navigator.open_config_file)
        btn_source.installEventFilter(self)
        return btn_source

    def back(self):
        self.hide()
        self.navigator.open_project_management_window()

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.navigator.open_project_management_window()
        return super().closeEvent(a0)

    def eventFilter(self, o, e):
        if e.type() == QEvent.Move:
            # if o is self.uic.btn_add:
            #     self.p1 = self.uic.btn_add.pos()
            # elif o is self.uic.btn_destination:
            #     self.p2 = self.uic.btn_destination.pos()
            self.update()
        return super().eventFilter(o, e)

    def paintEvent(self, event):
        painter = QPainter(self)
        btn_des = self.uic.btn_destination.geometry()
        x_des = btn_des.x()
        y_des = btn_des.y() + btn_des.height()/2
        for idx, btn in enumerate(self.uic.list_btn_source):
            btn_source_geo = btn.geometry()
            x_source = btn_source_geo.x() + btn_source_geo.width()
            y_source = btn_source_geo.y() + btn_source_geo.height()
            painter.drawLine(x_source, y_source, x_des, y_des)