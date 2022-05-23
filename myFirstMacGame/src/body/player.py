from ast import List, Str
from turtle import position
import keyboard
from src.body.body.bodyClass import body

class player(body):
    def __init__(self, positionX: int, positionY: int, defaultSkin: str, id: int, parentReference: object, collideWith: List):
        super().__init__( id, positionX, positionY, parentReference)

        if defaultSkin:
            self.defaultSkin = defaultSkin
        else:
            self.defaultSkin = "*"
        
        self.keyboard = keyboard

        self.newPositionX = 0
        self.newPositionY = 0

        self.moveX = 0
        self.moveY = 0

        self.collided = False

        self.collideWith = collideWith
    
    def doYourStuff(self, world, collision_world):
        self.newPositionX = self.positionX + self.moveX
        self.newPositionY = self.positionY + self.moveY

    def moveAndCollide(self, collision_world):
        self.collided = self.look_for_collision(collision_world, self.newPositionY, self.newPositionX)

        if (self.collided == False):
            self.positionX = self.newPositionX
            self.positionY = self.newPositionY
    
    def moveAndSlide(self, collision_world):
        self.collided = self.look_for_collision(collision_world, self.positionY, self.newPositionX)
        if (self.collided == False):
            self.positionX = self.newPositionX
        self.collided = self.look_for_collision(collision_world, self.newPositionY, self.positionX)
        if (self.collided == False):
            self.positionY = self.newPositionY

        
    
    def look_for_collision(self, collision_world, newPositionY, newPositionX):
        for y in collision_world[newPositionY][newPositionX]:
            
            if y.group in self.collideWith:
                
                return y.group
        return False