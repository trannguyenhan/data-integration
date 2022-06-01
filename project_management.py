from PyQt5.QtWidgets import QMainWindow
from ui.project_management import Ui_ProjectManagement
from new_project import NewProject

class ProjectManagement(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_ProjectManagement()
        self.uic.setupUi(self)
        self.uic.newproject_btn.clicked.connect(self.show_new_project_window)

    def show_new_project_window(self):
        win = NewProject(self)
        win.show()