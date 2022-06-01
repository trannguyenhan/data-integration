from PyQt5.QtWidgets import QMainWindow
from ui.new_project import Ui_NewProject
from dal import project_dao

class NewProject(QMainWindow):
    def __init__(self, parent=None):
        super(NewProject, self).__init__(parent)
        self.uic = Ui_NewProject()
        self.uic.setupUi(self)
        self.uic.okBtn.clicked.connect(self.ok_btn_clicked)

    def ok_btn_clicked(self):
        name = self.uic.lineEdit.text()
        if (name != ""):
            dest_type = self.uic.destinationCbx.currentText()
            project_dao.add_new_project(name, dest_type)
            self.parent().load_projects()
        self.close()