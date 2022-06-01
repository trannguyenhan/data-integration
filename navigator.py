from init_project import InitProject
from project_management import ProjectManagement

class Navigator:
    def __init__(self):
        self.init_project = InitProject(self)
        self.project_management = ProjectManagement(self)

    def open_init_project_window(self):
        self.init_project.show()
        self.project_management.hide()

    def open_project_management_window(self):
        self.project_management.show()