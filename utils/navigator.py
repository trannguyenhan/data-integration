from widgets import *
from .context import Context

class Navigator:
    '''
    Navigate windows
    '''
    def __init__(self):
        self.init_project = None
        self.project_management = ProjectManagement(self)
        self.workbench = None
        self.config_file = None
        self.preview = None

    def open_init_project_window(self):
        self.init_project = InitProject(self, Context.project)
        self.init_project.show()
        # self.project_management.hide()

    def open_project_management_window(self):
        self.project_management.show()

    def open_workbench(self):
        self.project_management.hide()
        self.workbench = Workbench(self)
        self.workbench.show()

    def open_config_file(self):
        self.config_file = ConfigFile(self)
        self.config_file.show()

    def open_preview(self, keys, datas):
        self.preview = Preview(self)
        self.preview.show_preview(keys=keys, datas=datas)
        self.preview.show()
