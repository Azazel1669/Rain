import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QTableWidget, QComboBox


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 200, 600, 230)
        self.setWindowTitle('Поиск по фильмам')

        self.parameterSelection = QComboBox(self)
        self.parameterSelection.addItems(['Год выпуска', 'Название', 'Продолжительность'])
        self.parameterSelection.resize(200, 27)
        self.parameterSelection.move(10, 10)

        if self.parameterSelection.currentTextChanged.connect('Год выпуска'):
            print(1)

        self.queryLine = QLineEdit(self)
        self.queryLine.resize(280, 27)
        self.queryLine.move(215, 10)

        self.queryButton = QPushButton("Поиск", self)
        self.queryButton.resize(70, 29)
        self.queryButton.move(500, 9)

        self.name_label0 = QLabel(self)
        self.name_label0.setText("ID:")
        self.name_label0.move(10, 40)

        self.name_label = QLabel(self)
        self.name_label.setText("Название:")
        self.name_label.move(10, 73)

        self.name_label1 = QLabel(self)
        self.name_label1.setText("Год выпуска:")
        self.name_label1.move(10, 109)

        self.name_label2 = QLabel(self)
        self.name_label2.setText("Жанр:")
        self.name_label2.move(10, 145)

        self.name_label3 = QLabel(self)
        self.name_label3.setText("Продолжительность:")
        self.name_label3.move(10, 184)
        self.name_label3.adjustSize()

        self.errorLabel = QLabel(self)
        self.errorLabel.setText("")
        self.errorLabel.move(10, 213)
        self.errorLabel.adjustSize()

        self.idEdit = QLineEdit(self)
        self.idEdit.resize(400, 23)
        self.idEdit.move(120, 40)

        self.titleEdit = QLineEdit(self)
        self.titleEdit.resize(400, 23)
        self.titleEdit.move(120, 73)

        self.yearEdit = QLineEdit(self)
        self.yearEdit.resize(400, 23)
        self.yearEdit.move(120, 109)

        self.genreEdit = QLineEdit(self)
        self.genreEdit.resize(400, 23)
        self.genreEdit.move(120, 145)

        self.durationEdit = QLineEdit(self)
        self.durationEdit.resize(400, 23)
        self.durationEdit.move(120, 184)


        # self.parameterSelection.setHorizontalHeaderLabels(['Название', 'Жанр', 'Год'])

        # self.parameterSelection = QTableWidget(self)
        # self.parameterSelection.setColumnCount(3)
        # self.parameterSelection.setHorizontalHeaderLabels(['Название', 'Жанр', 'Год'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())