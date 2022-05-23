from turtle import shape
from typing import List

from numpy import append, true_divide
from src.body.body.bodyClass import body
from src.body.collision_dot import collisionDot


class collisionToMapShape(body):
    def __init__(self, id: int, positionX: int, positionY: int, parentReference: object,  shape: List, group: str, positionFromParentX=0, positionFromParentY=0,):
        super().__init__(id, positionX, positionY, parentReference, positionFromParentX, positionFromParentY)

        self.shape = shape
        self.group = group

        self.filled = False
        
        self.pastIndex = []
        self.pastX = 0
        self.pastY = 0

    def doYourStuff(self, world, collision_world):
        
        self.fillWorld(collision_world,)
        self.pastX =self.positionX
        self.pastY = self.positionY
        super().doYourStuff(world, collision_world)
    
    def fillWorld(self, collision_world):
        if self.filled:
            for y in range(len(self.shape)):
                for x in range(len(self.shape[y])):
                    collision_world[self.pastY + y][self.pastX + x].pop(self.pastIndex[y][x] - 1)

        self.pastIndex.clear()

        for y in range(len(self.shape)):
            self.pastIndex.append([])
            for x in range(len(self.shape[y])):
                collision_world[self.positionY + y][self.positionX + x].append(collisionDot(0, self.positionX + x, self.positionY + y, self, self.group))
                self.pastIndex[y].append(len(collision_world[self.positionY + y][self.positionX + x]))
        self.filled = True
