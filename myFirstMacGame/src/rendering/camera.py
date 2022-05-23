

class camera:
    def __init__(self, height: int, width: int):

        self.heigth = height
        self.width = width

        self.positionFromAnchorX = 0
        self.positionFromAnchorY = 0

        self.anchorPositionX = 0
        self.anchorPositionY = 0

    def draw(self, world):
        for y in range(self.heigth):
            for x in range(self.width):
                if (y + self.anchorPositionY + self.positionFromAnchorY < len(world) and x + self.anchorPositionX + self.positionFromAnchorX < len(world[y]) and y + self.anchorPositionY + self.positionFromAnchorY > 0 and x + self.anchorPositionX + self.positionFromAnchorX > 0):
                    print(world[round(y + self.anchorPositionY)][x + self.anchorPositionX], end="")
                else:
                    print(" ", end="")
            print("")