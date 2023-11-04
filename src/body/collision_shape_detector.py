from ast import List, Str
from src.body.body.bodyClass import Body
from src.body.player import Player

class collision_shape_detector(Body):
    def __init__(self, id: int, positionX: int, positionY: int, parentReference: Player, shape: List, collideWith: List):
        super().__init__(id, positionX, positionY, parentReference)

        self.shape = shape

        self.collideWith = collideWith
        self.collided = False

        self.defaultSkin = " "

    def look_for_collision(self, collision_world, positionX, positionY):
        for y in range(len(self.shape)):
            for x in range(len(self.shape[y])):
                if (self.shape[y][x]):
                    self.collided = self._look_for_collision(collision_world, positionY + y, positionX + x)
                    if self.collided != False:
                        return self.collided

        return False
                        
    
    def _look_for_collision(self, collision_world, newPositionY, newPositionX):
        for y in collision_world[newPositionY][newPositionX]:         
            if y.group in self.collideWith:
                
                return y.group
        return False