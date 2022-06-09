from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from ui.project_management import Ui_ProjectManagement
from widgets.new_project import NewProject
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
        # Read from database
        self.uic.tableWidget.setRowCount(0)
        projects = project_dao.get_project_list()

        # Fill into table
        self.uic.tableWidget.setRowCount(len(projects))
        for i, project in enumerate(projects):
            name = project["project name"]
            type = project["destination type"]
            item = QTableWidgetItem(name)
            self.uic.tableWidget.setItem(i, 0, item)
            item = QTableWidgetItem(type)
            self.uic.tableWidget.setItem(i, 1, item)


    def show_new_project_window(self):
        win = NewProject(self)
        win.show()

    def open_project(self):
        # Get selected project
        selected_items = self.uic.tableWidget.selectedItems()
        if len(selected_items) == 0:
            return
        prj_name = selected_items[0].text()
        project = project_dao.get_by_name(prj_name)

        # Check if project is not init, open init window, else, open workbench
        is_initialized = project["is initialized"]
        if (is_initialized):
            self.navigator.open_workbench()
        else:
            self.navigator.open_init_project_window(project)