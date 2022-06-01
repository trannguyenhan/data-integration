from PyQt5.QtWidgets import QMainWindow, QListWidgetItem
from ui.project_management import Ui_ProjectManagement
from new_project import NewProject
from dal import project_dao

class ProjectManagement(QMainWindow):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator
        self.uic = Ui_ProjectManagement()
        self.uic.setupUi(self)
        self.uic.newproject_btn.clicked.connect(self.show_new_project_window)
        self.uic.open_btn.clicked.connect(self.open_project)
        self.load_projects()

    def load_projects(self):
        self.uic.listWidget.clear()
        projects = project_dao.get_project_list()
        for (project_id, project_name, destination) in projects:
            item = QListWidgetItem(f"{project_name} -> {destination}")
            self.uic.listWidget.addItem(item)

    def show_new_project_window(self):
        win = NewProject(self)
        win.show()

    def open_project(self):
        self.navigator.open_init_project_window()