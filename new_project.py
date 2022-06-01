from PyQt5.QtWidgets import QMainWindow
from ui.new_project import Ui_NewProject

class NewProject(QMainWindow):
    def __init__(self, parent=None):
        super(NewProject, self).__init__(parent)
        self.uic = Ui_NewProject()
        self.uic.setupUi(self)
        

