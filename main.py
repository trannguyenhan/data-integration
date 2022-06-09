from PyQt5.QtWidgets import QApplication
import sys
from navigator import Navigator
import db # Init class Database

if __name__ == "__main__":
    app = QApplication(sys.argv)
    navigator = Navigator()
    navigator.open_project_management_window()
    sys.exit(app.exec_())
    

