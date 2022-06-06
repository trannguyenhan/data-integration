from PyQt5.QtWidgets import QMainWindow
from ui.preview import Ui_Preview

class Preview(QMainWindow):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator
        self.uic = Ui_Preview()
        self.uic.setupUi(self)
        self.uic.okButton.clicked.connect(self.ok_btn_clicked)

    def ok_btn_clicked(self):
        self.navigator.preview.hide()