import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel

a = ['1', '2', '3', '4', '5', '6.py', '7', '8', '9', '0', '-']


class FileStat(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 160, 600, 170)
        self.setWindowTitle('Файловая статистика')

        self.name_label = QLabel(self)
        self.name_label.setText("Имя файла")
        self.name_label.move(10, 5)

        self.filenameEdit = QLineEdit(self)
        self.filenameEdit.resize(85, 25)
        self.filenameEdit.move(150, 10)

        self.button = QPushButton("Рассчитать", self)
        self.button.resize(70, 25)
        self.button.move(240, 10)
        self.button.clicked.connect(self.do_do)

        self.name_label1 = QLabel(self)
        self.name_label1.setText("Миниальное значение:")
        self.name_label1.adjustSize()
        self.name_label1.move(10, 50)

        self.minEdit = QLineEdit("0", self)
        self.minEdit.resize(85, 25)
        self.minEdit.move(150, 45)

        self.name_label2 = QLabel(self)
        self.name_label2.setText("Максимальное значение:")
        self.name_label2.adjustSize()
        self.name_label2.move(10, 85)

        self.maxEdit = QLineEdit("0", self)
        self.maxEdit.resize(85, 25)
        self.maxEdit.move(150, 80)

        self.name_label3 = QLabel(self)
        self.name_label3.setText("Среднее значение:")
        self.name_label3.adjustSize()
        self.name_label3.move(10, 120)

        self.avgEdit = QLineEdit("0,00", self)
        self.avgEdit.resize(85, 25)
        self.avgEdit.move(150, 115)

        self.statusBar()

    def do_do(self):
        try:
            with open(self.filenameEdit.text(), 'r') as f:
                line = (("".join(f.readline())).replace("\\n", " ").replace("\\t", " ").replace('"', "")).split()
                print(line)
                line1 = []
                for i in line:
                    p = 0
                    f = 0
                    for j in i:
                        if j not in a:
                            p = 1
                            break
                        if j.lower() in "qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролдэячсмитьбюё":
                            f = 1
                            break
                    if p == 0:
                        line1.append(int(i))
                print(line1)
                if f == 1:
                    self.statusBar().showMessage("Файл содержит некорректные данные")
                elif line1 != []:
                    a1 = str(max(line1))
                    b = str(min(line1))
                    c = str(round((sum(line1) / len(line1)), 2))
                    print(sum(line1), len(line1), round((sum(line1) / len(line1)), 2))
                    self.maxEdit.setText(a1)
                    self.minEdit.setText(b)
                    self.avgEdit.setText(c)
                    with open("out.txt", 'w', encoding="UTF-8") as e:
                        print(f'Максимальное значение = {a1}', file=e)
                        print(f"Минимальное начение = {b}", file=e)
                        print(f'Среднее значение = {c}', file=e)
                else:
                    self.statusBar().showMessage("Указанный файл пуст")
        except FileNotFoundError:
            self.statusBar().showMessage("Указанный файл не существет")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileStat()
    ex.show()
    sys.exit(app.exec())
