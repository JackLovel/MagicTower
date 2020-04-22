from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, \
    qApp, QLabel, QVBoxLayout, QHBoxLayout, QWidget

class GameLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.img = QPixmap()

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.img = self.pixmap()

    def wheelEvent(self, event):
        pass

    def mouseDoubleClickEvent(self, event):
        pass

    def mouseReleaseEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        pass



