import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class GameImage:
    def __init__(self, name):
        self.image = {
            # player
            "left": "img/player/left.png",
            "right": "img/player/right.png",
            "front": "img/player/front.png",
            "back": "img/player/back.png",
            # wall
            "w0": 'img/wall/w1.png',
            "w1": 'img/wall/w2.png',
            "w2": 'img/wall/w3.png',
            "w3": 'img/wall/w4.png',
            "w4": 'img/wall/w5.png',
            "w5": 'img/wall/w6.png',
            "w6": 'img/wall/w7.png',
            "w7": 'img/wall/w8.png',
            "w8": 'img/wall/w9.png',
            "w9": 'img/wall/w10.png',
        }
        self.img = self.imageFromPath(name)
        self.w = 60
        self.h = 60
        self.x = 60
        self.y = 60

    def imageFromPath(self, name):
        n = self.image[name]
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), n)
        return path


class Wall(GameImage):
    def __init__(self, name):
        super().__init__(name)
        self.w = 50
        self.h = 50
        self.x = 50
        self.y = 50


class Player(GameImage):
    def __init__(self, name):
        super().__init__(name)
        self.speed = 50

    def moveRight(self):
        self.x += self.speed
        if self.x > 750:
            self.x = 750

    def moveLeft(self):
        self.x -= self.speed
        if self.x < 50:
            self.x = 50

    def moveUp(self):
        self.y -= self.speed

    def moveDown(self):
        self.y += self.speed


class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.player = Player('back')
        self.wall = Wall('w1')
        self.wall.x = 200
        self.wall.y = 200

    def initUi(self):
        self.move(300, 200)
        self.resize(900, 700)
        self.setWindowTitle('魔塔')
        self.show()

    def keyPressEvent(self, event):
        p = self.player
        k = event.key()
        if k == Qt.Key_D:
            p.moveRight()
        elif k == Qt.Key_A:
            p.moveLeft()
        elif k == Qt.Key_W:
            p.moveUp()
        elif k == Qt.Key_S:
            p.moveDown()

        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen)
        qp.drawRect(50, 50, 800, 500)

        p = self.player
        img = QPixmap()
        img.load(p.img)
        qp.drawPixmap(p.x, p.y, p.w, p.h, img)

        w = self.wall
        img2 = QPixmap()
        img2.load(w.img)
        qp.drawPixmap(w.x, w.y, w.w, w.h, img2)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Game()
    sys.exit(app.exec_())
