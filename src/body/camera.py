from ast import boolop
from tokenize import Triple
from src.body.body.bodyClass import body

class camera(body):
    def __init__(self, id: int, positionX: int, positionY: int, parentReference: object, height: int, width: int,  positionFromParentX = 0, positionFromParentY = 0):
        super().__init__(id, positionX, positionY, parentReference,  positionFromParentX, positionFromParentY)

        self.heigth = height
        self.width = width
    def doYourStuff(self, world, collision_world):
        self.draw(world)

    def draw(self, world):
        for y in range(self.heigth):
            for x in range(self.width):
                if (y + self.positionY < len(world) and x + self.positionX < len(world[y]) and y + self.positionY > 0 and x + self.positionX > 0):
                    print(world[round(y + self.positionY)][x + self.positionX], end="")
                else:
                    print(" ", end="")
            print("")