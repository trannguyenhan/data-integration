from PyQt5.QtWidgets import QMainWindow, QListWidgetItem
from ui.project_management import Ui_ProjectManagement
from new_project import NewProject
from dal import project_dao

class ProjectManagement(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_ProjectManagement()
        self.uic.setupUi(self)
        self.uic.newproject_btn.clicked.connect(self.show_new_project_window)
        self.load_projects()

    def load_projects(self):
        self.uic.listWidget.clear()
        projects = project_dao.get_project_list()
        for (project_id, project_name) in projects:
            item = QListWidgetItem(project_name)
            self.uic.listWidget.addItem(item)

    def show_new_project_window(self):
        win = NewProject(self)
        win.show()