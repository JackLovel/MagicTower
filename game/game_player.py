from game.game_image import GameImage


class GamePlayer(GameImage):
    def __init__(self, name):
        super().__init__(name)
        self.speed = 60
        self.mapWidth = 780
        self.mapHeight = 480
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
