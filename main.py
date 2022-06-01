from PyQt5.QtWidgets import QApplication
import sys
from project_management import ProjectManagement

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ProjectManagement()
    win.show()
    sys.exit(app.exec_())