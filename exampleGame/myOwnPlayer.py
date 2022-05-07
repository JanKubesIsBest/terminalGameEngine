
from ast import List
from tokenize import group
from src.body.player import player
from src.body.kinematic_body import kinematic_body
from src.body.collision_shape_detector import collision_shape_detector

from walkingAnimation import walkingAnimation
from wstojim import stojimAnimation

from myAGAME import myOwnGame

class myOwnPlayer(player):
    def __init__(self, positionX, positionY, defaultSkin, id, parentReference: myOwnGame, collideWith: List):
        super().__init__(positionX, positionY, defaultSkin, id, parentReference, collideWith)

        self.add_new_child("sprite", kinematic_body(self.positionX, self.positionY, " ", len(self.childs), self,animate=True, animations=[walkingAnimation("walking"), stojimAnimation("stoji")], firstAnimation="stoji"))

        self.collisionShape = [
            [False, True, False],
            [False, True, False],
            [True, True, True],
        ]
        self.add_new_child("collisionShape", collision_shape_detector(len(self.childs), self.positionX, self.positionY, self, shape=self.collisionShape, collideWith=collideWith))

        self.myKinematicBodyReference = self.childs[0][2]
        self.is_walking = False

        self.moveX = 0
        self.moveY = 0

    def doYourStuff(self, world, collision_world):
        self.moveY = self.parentReference.gravity
        
        self.moveX = int(self.keyboard.is_pressed("d")) - int(self.keyboard.is_pressed("a"))

        if self.moveX == 0:
            #reference to the kinematic body 
            self.myKinematicBodyReference.changeAnimation("stoji")
        if self.moveX == 1 or self.moveX == -1:
            self.myKinematicBodyReference.changeAnimation("walking")

        super().doYourStuff(world, collision_world)

        self.moveAndSlide(collision_world)
        

    def look_for_collision(self, collision_world, newPositionY, newPositionX):
        return self.childs[1][2].look_for_collision(collision_world, newPositionX, newPositionY)

        

    def doStuffWithUpdatedChild(self, child):
        child.positionX = self.positionX
        child.positionY = self.positionY

    def add_new_child(self, object_name, object_reference):
        return super().add_new_child(object_name, object_reference)