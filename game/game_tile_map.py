from game.game_image import GameImage


class GameTileMap:
    def __init__(self):
        self.tiles = [
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 1, 0, 0, 0,
            0, 1, 0, 1, 1, 0, 0, 0,
            0, 1, 0, 1, 1, 0, 0, 0,
            0, 1, 0, 1, 1, 0, 0, 0,
            0, 1, 0, 1, 1, 0, 0, 0,
            0, 1, 0, 1, 1, 0, 0, 0,
            0, 1, 0, 1, 1, 0, 0, 0,
            0, 0, 0, 1, 1, 0, 0, 0,
        ]
        self.th = 8
        self.tw = len(self.tiles) / self.th
        self.tileImages = [
            GameImage('w0'),
            GameImage('w1'),
            GameImage('w2'),
            GameImage('w3'),
        ]
        self.tileSize = 60
