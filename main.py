import math
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, qApp

from game.game_tile_map import GameTileMap
from game.game_player import GamePlayer
from game.config import Config
from game.game_image import GameImage
from map_editor.map_editor import MapEditor

class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.mapWidth = Config.mapWidth
        self.mapHeight = Config.mapHeight
        self.offsetX = Config.mapOffsetX
        self.offsetY = Config.mapOffsetY
        self.player = GamePlayer('back')
        self.player.x = self.mapWidth / 2 - self.player.w / 2 + self.offsetX
        self.player.y = self.mapHeight - self.player.h + self.offsetY
        # self.imgs = GameImage.allImage()
        self.map = GameTileMap()
        # self.mapEditor = MapEditor()

    def initUi(self):
        self.setup()
        self.move(300, 200)
        self.resize(900, 700)
        self.setWindowTitle('魔塔')
        self.show()

    def setup(self):
        self.setupMenu()

    def setupMenu(self):
        exitAct = QAction('退出', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出程序')
        exitAct.triggered.connect(qApp.quit)

        mapEditorAct = QAction('打开地图编辑器', self)
        mapEditorAct.setStatusTip('打开地图编辑器')
        # exitAct.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件')
        fileMenu.addAction(exitAct)
        fileMenu.addAction(mapEditorAct)

        self.statusBar()


    def keyPressEvent(self, event):
        p = self.player
        k = event.key()
        if k == Qt.Key_D or k == Qt.Key_Right:
            p.moveRight()
        elif k == Qt.Key_A or k == Qt.Key_Left:
            p.moveLeft()
        elif k == Qt.Key_W or k == Qt.Key_Up:
            p.moveUp()
        elif k == Qt.Key_S or k == Qt.Key_Down:
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

        m = self.map
        size = len(m.tiles)
        for i in range(size):
            ii = m.tiles[i]
            im = m.tileImages[ii].img
            x = math.floor(i / m.th) * m.tileSize + self.offsetX
            y = math.floor(i % m.th) * m.tileSize + self.offsetY
            qp.drawPixmap(x, y, m.tileSize, m.tileSize, im)

        p = self.player
        qp.drawPixmap(p.x, p.y, p.w, p.h, p.img)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Game()
    sys.exit(app.exec_())
