from turtle import width
from src.body.body.bodyClass import body
from src.body.collision_dot import collisionDot

class TileMap(body):
    def __init__(self, id: int, positionX: int, positionY: int, parentReference: object, name: str, group: str, heigth: int, width: int, tileSkin: str):
        super().__init__(id, positionX, positionY, parentReference)
        self.heigth = heigth
        self.width = width

        self.group = group

        if len(tileSkin) > 0:
            self.defaultSkin = ""
            self.tileSkin = tileSkin

    def doYourStuff(self, world, collision_world):
        self.draw(world)
        pass
    def draw(self, world):
        for y in range(self.heigth):
            for x in range(self.width):
                if self.positionY + y <= len(world) and  self.positionX + x < len(world[y]):
                    world[self.positionY + y][self.positionX + x] = self.tileSkin

    def fill_world(self, collision_world, world):
        for y in range(self.heigth):
            for x in range(self.width):
                if self.positionY + y <= len(world) and  self.positionX + x < len(world[y]):
                    collision_world[self.positionY + y][self.positionX + x].append(collisionDot(len(self.childs), self.positionX + x, self.positionY + y, self, self.group))
