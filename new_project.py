from PyQt5.QtWidgets import QMainWindow
from matplotlib.pyplot import close
from ui.new_project import Ui_NewProject
from dal import project_dao

class NewProject(QMainWindow):
    def __init__(self, parent=None):
        super(NewProject, self).__init__(parent)
        self.uic = Ui_NewProject()
        self.uic.setupUi(self)
        self.uic.pushButton.clicked.connect(self.add_new_project)

    def add_new_project(self):
        name = self.uic.lineEdit.text()
        project_dao.add_new_project(name)
        self.parent().load_projects()
        self.close()