class Config:
    # tile
    imgWidth = 60
    imgHeight = 60
    imgX = 60
    imgY = 60
    # map
    mapSize = 11 # 11 x 11 
    mapWidth = imgWidth * mapSize
    mapHeight = imgHeight * mapSize
    mapOffsetX = 50
    mapOffsetY = 50
    # player
    playerSpeed = 60
    # version
    python_version = '3.7'
    pyqt5_version = '5.12.3'


if __name__ == '__main__':
    print(Config.mapWidth)
