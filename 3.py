import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect("films_db.sqlite")
        # self.pushButton.clicked.connect(self.select)

        s1 = "year " + str(self.lineEdit.text())
        s2 = "title " + str(self.lineEdit_2.text())
        s3 = "duration " + str(self.lineEdit_3.text())
        print(1, s1)
        print(s2)
        print(s3)
        req = str("SELECT * FROM Films WHERE " + s1 + " AND " + s2 + " AND " + s3)
        req = '"""' + req + '"""'
        print(req)
        print(2)
        cur = self.con.cursor()

        result = cur.execute(req).fetchall()

        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(3)

        print(3)
        for i, elem in enumerate(result):
            for j in range(len(elem) - 2):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem[j])))
        self.tableWidget.setHorizontalHeaderLabels(['Название', 'Жанр', 'Год'])
        print(1)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
