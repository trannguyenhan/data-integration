from PyQt5.QtWidgets import QWidget
from ui.workbench import Ui_workbench
from PyQt5.QtGui import QCloseEvent

class Workbench(QWidget):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator
        self.uic = Ui_workbench()
        self.uic.setupUi(self)
    
    def closeEvent(self, a0: QCloseEvent) -> None:
        self.navigator.open_project_management_window()
        return super().closeEvent(a0)