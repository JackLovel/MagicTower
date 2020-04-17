import math
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QWidget, QApplication

from game.game_tile_map import GameTileMap
from game.game_player import GamePlayer


class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.mapWidth = 800
        self.mapHeight = 500
        self.offsetX = 50
        self.offsetY = 50
        self.player = GamePlayer('back')
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

        p = self.player
        qp.drawPixmap(p.x, p.y, p.w, p.h, p.img)

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
