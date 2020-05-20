import math
import sys
import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QPixmap, QMouseEvent
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, \
    qApp, QLabel, QVBoxLayout, QHBoxLayout, QWidget

from game.game_tile_map import GameTileMap
from game.game_player import GamePlayer
from game.config import Config
from game.game_image import GameImage
from game.game_label import GameLabel


class MapEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        vLayout = QVBoxLayout()
        vLayout.setSpacing(2)  # 设置控件间距
        self.mx = 100
        self.my = 20
        self.mw = 660
        self.mh = 660
        self.tileSize = 60
        widget = QWidget()
        self.img = {
            # player
            "left": "../img/player/left.png",
            "right": "../img/player/right.png",
            "front": "../img/player/front.png",
            "back": "../img/player/back.png",
            # wall
            "w0": '../img/wall/w1.png',
            "w1": '../img/wall/w2.png',
            "w2": '../img/wall/w3.png',
            "w3": '../img/wall/w4.png',
            "w4": '../img/wall/w5.png',
            "w5": '../img/wall/w6.png',
            "w6": '../img/wall/w7.png',
            "w7": '../img/wall/w8.png',
            "w8": '../img/wall/w9.png',
            "w9": '../img/wall/w10.png',
        }

        tile = self.img.keys()
        for t in tile:
            img = self.imgByName(t)
            l = GameLabel()
            l.setPixmap(img)
            vLayout.addWidget(l)

        widget.setLayout(vLayout)
        self.setCentralWidget(widget)

        self.move(300, 200)
        self.resize(900, 700)
        self.setWindowTitle('地图编辑器')
        self.show()

    # def setupMap(self):
    #     self.tileMap = [
    #
    #     ]

    def imgByName(self, name):
        i = QPixmap()
        n = self.img[name]
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), n)
        i.load(path)
        return i

    def setupMenu(self):
        pass

    def addTile(self, x, y):
        pass

    def inMap(self, mouseX, mouseY):
        x = mouseX
        y = mouseY
        xIn = self.mx <= x and x <= self.mx + self.mw
        yIn = self.my <= y and y <= self.my + self.mh
        return xIn and yIn

    def mousePressEvent(self, event: QMouseEvent):
        x = event.pos().x()
        y = event.pos().y()
        i = math.floor((x - self.mx) / self.tileSize)
        j = math.floor((y - self.my) / self.tileSize)
        if self.inMap(x, y):
            print('x, y', x, y, i, j)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.drawText(770, 20, "地图坐标: ({}, {}), 地图宽度：({}， {})".format(self.mx, self.my, self.mw, self.mh))
        painter.drawRect(self.mx, self.my, self.mw, self.mh)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = MapEditor()
    sys.exit(app.exec_())
