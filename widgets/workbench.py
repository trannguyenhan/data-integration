from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QCloseEvent, QPainter
from PyQt5.QtWidgets import QMainWindow, QWidget
from ui.workbench import Ui_Workbench


class Drawer:
    def paintEvent(self, event):
        painter = QPainter(self)
        btn_des = self.uic.btn_destination.geometry()
        x_des = btn_des.x()
        y_des = btn_des.y() + btn_des.height()/2

        for  idx, btn in enumerate(self.listInputSource):
            btn_source = getattr(self.uic,"btn_input_source_"+str(idx)).geometry()
            x_source = btn_source.x()+btn_source.width()
            y_source = btn_source.y() + btn_source.height()
            painter.drawLine(x_source, y_source, x_des, y_des)

class Workbench(QWidget,Drawer):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator
        self.uic = Ui_Workbench()
        self.listInputSource = []
        self.type_inputs = [
            # {'California': ['San Francisco', 'Oakland', 'San Jose', 'San Mateo']},
            # {'Illinois': ['Chicago', 'Evanston', 'Springfield']},
            'CSV',
            'JSON',
            "XML",
            "Flat File",
            "MySQL"
        ]
        self.uic.setupUi(self)
        print("gehe")


    def eventFilter(self, o, e):
        if e.type() == QEvent.Move:
            # if o is self.uic.btn_add:
            #     self.p1 = self.uic.btn_add.pos()
            # elif o is self.uic.btn_destination:
            #     self.p2 = self.uic.btn_destination.pos()
            self.update()
        return super().eventFilter(o, e)

    def add_input_source(self,source):
        print(source.text())
        self.listInputSource.append(source.text())
        self.uic.renderInputList(self)

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.navigator.open_project_management_window()
        return super().closeEvent(a0)
