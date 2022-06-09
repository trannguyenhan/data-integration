from PyQt5.QtWidgets import QMainWindow,QFileDialog
from ui.config_file import Ui_ConfigFile
from dal import project_dao
from PyQt5.QtGui import QCloseEvent
class ConfigFile(QMainWindow):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator
        self.uic = Ui_ConfigFile()
        self.uic.setupUi(self)
        self.uic.okButton.clicked.connect(self.ok_btn_clicked)
        self.uic.browseFileButton.clicked.connect(self.browse_file)
        self.uic.previewButton.clicked.connect(self.preview)

    def ok_btn_clicked(self):
        self.navigator.open_workbench()
        self.navigator.config_file.hide()

    def browse_file(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        with open(path, "r") as f:
            print(f.readline())

    def preview(self):
        self.navigator.open_preview()

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.navigator.open_workbench()
        return super().closeEvent(a0)
