import os
from PyQt5.QtGui import QPainter, QPixmap, QPen
from game.config import Config


class GameImage:
    def __init__(self, name):
        self.name = name
        self.image = {
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
        self.img = self.imageFromPath(name)
        self.w = Config.imgWidth
        self.h = Config.imgHeight
        self.x = Config.imgX
        self.y = Config.imgY

    def imageFromPath(self, name):
        i = QPixmap()
        n = self.image[name]
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), n)
        i.load(path)
        return i