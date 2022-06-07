from PyQt5.QtWidgets import QApplication
import sys

import db
from navigator import Navigator

if __name__ == "__main__":
    app = QApplication(sys.argv)
    navigator = Navigator()
    navigator.open_project_management_window()
    sys.exit(app.exec_())

