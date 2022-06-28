from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from ui.preview import Ui_Preview
from my_engine import EngineCsv, EngineJson, EngineXml

class Preview(QMainWindow):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator
        self.uic = Ui_Preview()
        self.uic.setupUi(self)
        self.uic.okButton.clicked.connect(self.ok_btn_clicked)

    def show_preview(self, keys, datas):
        print(keys)
        row_count = 10 if len(datas) >= 10 else len(datas)
        self.uic.tableWidget.setColumnCount(len(keys))
        for i in range(len(keys)):
            self.uic.tableWidget.setColumnWidth(i, 153)
        self.uic.tableWidget.setRowCount(row_count)
        print("======================")
        print(keys)
        self.uic.tableWidget.setHorizontalHeaderLabels(keys)
        i=0
        for data in datas:
            print(data)
            j = 0
            for(key,value) in data.items():
                print(key,value)
                item = QTableWidgetItem()
                item.setText(str(value))
                self.uic.tableWidget.setItem(i, j, item)
                j+=1
            i+=1
        # self.navigator.open_preview()

    def ok_btn_clicked(self):
        self.navigator.preview.hide()