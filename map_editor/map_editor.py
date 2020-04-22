import math
import sys
import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, \
    qApp, QLabel, QVBoxLayout, QHBoxLayout, QWidget

from game.game_tile_map import GameTileMap
from game.game_player import GamePlayer
from game.config import Config
from game.game_image import GameImage

class MapEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setup()
        self.move(300, 200)
        self.resize(900, 700)
        self.setWindowTitle('地图编辑器')
        self.show()

    def setup(self):
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

        vLayout = QVBoxLayout()
        widget = QWidget()

        label1 = QLabel()
        img = self.imgByName("w0")
        label1.setPixmap(img)

        label2 = QLabel()
        img = self.imgByName("w1")
        label2.setPixmap(img)

        vLayout.addWidget(label1)
        vLayout.addWidget(label2)
        # vLayout.setSpacing(2)  # 设置控件间距
        widget.setLayout(vLayout)
        self.setCentralWidget(widget)
        # self.setLayout(vLayout)


    def imgByName(self, name):
        i = QPixmap()
        n = self.img[name]
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), n)
        i.load(path)
        return i

    def setupMenu(self):
        pass


    def keyPressEvent(self, event):
        pass

    def paintEvent(self, event):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = MapEditor()
    sys.exit(app.exec_())