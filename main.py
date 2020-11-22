import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Рисование')
        self.btnspawn = QPushButton('Появление', self)
        self.btnspawn.move(0, 577)
        self.btnspawn.resize(800, 23)
        self.btnspawn.clicked.connect(self.on_click)
        self.btnspawn = False

    def on_click(self):
        self.btnspawn = True
        self.repaint()

    def draw_ellips(self, qp):
        a = randint(30, 100)
        x = randint(100, 700)
        y = randint(100, 477)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        qp.setPen(QColor(r, g, b))
        qp.drawEllipse(x, y, a, a)

    def paintEvent(self, event):
        if self.btnspawn:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellips(qp)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
