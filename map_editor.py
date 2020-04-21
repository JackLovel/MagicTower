import math
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, qApp

from game.game_tile_map import GameTileMap
from game.game_player import GamePlayer
from game.config import Config

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
        pass

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