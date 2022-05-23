
from ast import List
from src.body.player import player
from src.body.kinematic_body import kinematic_body
from src.body.collision_shape_detector import collision_shape_detector

from walkingAnimation import walkingAnimation
from wstojim import stojimAnimation

from myAGAME import myOwnGame
from myOwnBullet import myBullet

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

        self.coldown_for_pistol = 3
        self.bulletDirection = 1

    def doYourStuff(self, world, collision_world):

        if (self.coldown_for_pistol != 3):
            self.coldown_for_pistol += 1
        
        self.moveY = self.parentReference.gravity
        
        self.moveX = int(self.keyboard.is_pressed("d")) - int(self.keyboard.is_pressed("a"))

        if self.moveX == 0:
            #reference to the kinematic body 
            self.myKinematicBodyReference.changeAnimation("stoji")
        if self.moveX == 1 or self.moveX == -1:
            self.bulletDirection = self.moveX
            self.myKinematicBodyReference.changeAnimation("walking")
        
        if self.keyboard.is_pressed("s") and self.coldown_for_pistol == 3:
            self.coldown_for_pistol = 0

            bullet_speed = self.bulletDirection
            self.parentReference.add_new_child("Bullet" + str(len(self.parentReference.all_objects)), myBullet(len(self.parentReference.all_objects), self.positionX + bullet_speed, self.positionY + 1, self.parentReference, bullet_speed))

        super().doYourStuff(world, collision_world)

        self.moveAndSlide(collision_world)
        

    def look_for_collision(self, collision_world, newPositionY, newPositionX):
        return self.childs[1][2].look_for_collision(collision_world, newPositionX, newPositionY)

    def add_new_child(self, object_name, object_reference):
        return super().add_new_child(object_name, object_reference)