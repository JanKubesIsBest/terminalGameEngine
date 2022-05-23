from numpy import true_divide
from src.body.player import player
from src.body.collision_shape_detector import collision_shape_detector

from ast import List

class myOwnTarget(player):
    def __init__(self, positionX: int, positionY: int, defaultSkin: str, id: int, parentReference: object, collideWith: List):
        super().__init__(positionX, positionY, defaultSkin, id, parentReference, collideWith)

        self.shape = [[True]]
        self.add_new_child("collisionShape", collision_shape_detector(len(self.childs), self.positionX, self.positionY, self, self.shape, collideWith))
    
    def doYourStuff(self, world, collision_world):
        for dot in collision_world[self.positionY][self.positionX]:
            if dot.group in self.collideWith:
                self.parentReference.points += 1

