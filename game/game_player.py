from game.game_image import GameImage
from game.config import Config


class GamePlayer(GameImage):
    def __init__(self, name):
        super().__init__(name)
        self.speed = Config.playerSpeed
        # 地图相关的属性
        self.mw = Config.mapWidth
        self.mh = Config.mapHeight
        self.mx = Config.mapOffsetX
        self.my = Config.mapOffsetY

    def moveRight(self):
        self.x += self.speed
        if self.x > self.mx + self.mw - self.w:
            self.x = self.mx + self.mw - self.w

    def moveLeft(self):
        self.x -= self.speed
        if self.x < self.mx:
            self.x = self.mx

    def moveUp(self):
        self.y -= self.speed
        if self.y < self.my:
            self.y = self.my

    def moveDown(self):
        self.y += self.speed
        if self.y > self.my + self.mh - self.h:
            self.y = self.my + self.mh - self.h
