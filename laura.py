import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
import json


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("design.ui", self)
        self.btnadd.clicked.connect(self.add_task)
        self.btnremove.clicked.connect(self.remove_task)
        self.load_tasks()

    def add_task(self):
        task = self.lineEdit.text()
        if task:
            self.listWidget.addItem(task)
            self.lineEdit.clear()
            self.save_task()

    def remove_task(self):
        selected_task = self.listWidget.selectedItems()
        if selected_task:
            for task in selected_task:
                self.listWidget.takeItem(self.listWidget.row(task))
            self.save_task()

    def load_tasks(self):
        try:
            with open("task.json", "r") as file:
                tasks = json.load(file)
                for task in tasks:
                    self.listWidget.addItem(task)
        except FileNotFoundError:
            pass

    def save_task(self):
        task = [self.listWidget.item(i).text() for i in range(self.listWidget.count())]
        with open("task.json", "w") as file:
            json.dump(task, file)


app = QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle("To Do List")
window.show()
sys.exit(app.exec_())
