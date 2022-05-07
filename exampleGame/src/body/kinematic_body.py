from re import S
from src.body.body.bodyClass import body

class kinematic_body(body):
    #if there is only single frame (sprite), animate should be called false and in animations only one 2d array
    def __init__(self, positionX, positionY, defaultSkin, id, parentReference, animate, animations , firstAnimation):
        super().__init__(id, positionX, positionY, parentReference)

        if defaultSkin:
            self.defaultSkin = defaultSkin
        else:
            self.defaultSkin = "="

        self.animate = animate
        self.animations = animations

        if self.animate:
            self.frames = []
            self.currentAnimation = self.searchForAnimation(firstAnimation)

            self.current_frame = 0

            self.name_of_current_animation = firstAnimation

        else:
            self.kinematicCanvas = animations


        parentReference.defaultSkin = ""
    
    

    def doYourStuff(self, world, collision_world):
        if self.animate:
            self.kinematicCanvas = self.frames[self.current_frame]
            if len(self.frames) - 1 != self.current_frame:
                self.current_frame += 1
            else:
                self.current_frame = 0

        for y in range(len(self.kinematicCanvas)):
            for x in range(len(self.kinematicCanvas)):
                world[self.positionY + y][self.positionX + x] = self.kinematicCanvas[y][x]
    
    def changeAnimation(self, nameOfNewAnimation):
        if (nameOfNewAnimation != self.name_of_current_animation):
            self.name_of_current_animation = nameOfNewAnimation
            self.currentAnimation = self.searchForAnimation(nameOfNewAnimation)

            self.current_frame = 0

    def searchForAnimation(self, nameOfAnimation):
        for x in self.animations:
            if x.animationName == nameOfAnimation:
                self.frames = x.animation
                return


    
    