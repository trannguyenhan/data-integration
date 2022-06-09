from PyQt5.QtWidgets import QApplication
import sys
from utils.navigator import Navigator
import database # Init class Database for connecting

if __name__ == "__main__":
    app = QApplication(sys.argv)
    navigator = Navigator()
    navigator.open_project_management_window()
    sys.exit(app.exec_())
    

