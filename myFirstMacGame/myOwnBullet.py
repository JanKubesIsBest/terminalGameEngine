from numpy import true_divide
from src.body.body.bodyClass import body
from src.body.collisionToMapShape import collisionToMapShape


class myBullet(body):
    def __init__(self, id: int, positionX: int, positionY: int, parentReference: object, speed: int, positionFromParentX=0, positionFromParentY=0):
        super().__init__(id, positionX, positionY, parentReference, positionFromParentX, positionFromParentY)

        self.speed = speed

        self.defaultSkin = ">"
        self.shape = [[True]]

        self.add_new_child("collisionAdder", collisionToMapShape(len(self.childs), self.positionX, self.positionY, self, self.shape, "bullet"))

    def doYourStuff(self, world, collision_world):
        #if self.positionY < len(world) and self.positionX < len(world[self.positionY]) and self.positionY > len(world) and self.positionX > len(world[self.positionY]):
        self.positionX += self.speed
