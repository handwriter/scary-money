from PyQt5.QtWidgets import QWidget, QApplication
from design import Ui_Form as Design
import csv
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
import sys
from PyQt5.QtGui import QColor
from random import choice

class Widget(QWidget, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        mass = []
        colors = ["red", "green", "blue", "grey", "orange", "yellow"]
        with open(QFileDialog.getOpenFileName()[0], encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for index, row in enumerate(reader):
                mass.append([int(row[1]), row[0]])
        mass = list(sorted(mass, reverse=True))
        mass = [[i[1], i[0]] for i in mass]
        self.tableWidget.setRowCount(len(mass))
        self.tableWidget.setColumnCount(2)
        for i in range(len(mass)):
            for j in range(len(mass[i])):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(mass[i][j])))
                if i < 5 and j == 0:
                    self.tableWidget.item(i, j).setForeground(QColor(choice(colors)))


app = QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())