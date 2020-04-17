import sys
import os
import math
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPixmap, QPen
from PyQt5.QtWidgets import QWidget, QApplication


class GameMap:
    def __init__(self):
        self.width = 15
        self.height = 20
        self.tiles = []
        self.setupTile()

    def setupTile(self):
        pass

    def setTile(self, i, j, tile):
        pass

    def exportJSON(self):
        pass


class GameImage:
    def __init__(self, name):
        self.name = name
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
        i = QPixmap()
        n = self.image[name]
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), n)
        i.load(path)
        return i


class GameTileMap:
    def __init__(self):
        self.tiles = [
            1, 0, 0, 1,
            1, 0, 0, 1,
        ]
        self.th = 4
        self.tw = len(self.tiles) / self.th
        self.tileImages = [
            GameImage('w0'),
            GameImage('w1'),
            GameImage('w2'),
            GameImage('w3'),
        ]
        self.tileSize = 60


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
        self.mapWidth = 800
        self.mapHeight = 500
        self.offsetX = 50
        self.offsetY = 50

    def moveRight(self):
        self.x += self.speed
        if self.x > self.offsetX + self.mapWidth - self.w:
            self.x = self.offsetX + self.mapWidth - self.w

    def moveLeft(self):
        self.x -= self.speed
        if self.x < self.offsetX:
            self.x = self.offsetX

    def moveUp(self):
        self.y -= self.speed
        if self.y < self.offsetY:
            self.y = self.offsetY

    def moveDown(self):
        self.y += self.speed
        if self.y > self.offsetY + self.mapHeight - self.h:
            self.y = self.offsetY + self.mapHeight - self.h


class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.mapWidth = 800
        self.mapHeight = 500
        self.offsetX = 50
        self.offsetY = 50
        self.player = Player('back')
        self.player.x = self.mapWidth / 2 - self.player.w / 2 + self.offsetX
        self.player.y = self.mapHeight - self.player.h + self.offsetY
        self.map = GameTileMap()

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
        qp.drawRect(self.offsetX, self.offsetY, self.mapWidth, self.mapHeight)

        # player
        p = self.player
        qp.drawPixmap(p.x, p.y, p.w, p.h, p.img)

        # map
        m = self.map
        size = len(m.tiles)
        for i in range(size):
            ii = m.tiles[i]
            im = m.tileImages[ii].img
            x = math.floor(i / m.th) * m.tileSize + self.offsetX
            y = math.floor(i % m.th) * m.tileSize + self.offsetY
            qp.drawPixmap(x, y, m.tileSize, m.tileSize, im)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Game()
    sys.exit(app.exec_())
