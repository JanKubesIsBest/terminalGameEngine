from src.body.body.bodyClass import body
from src.rendering.camera import camera

class viewport(body):
    def __init__(self, id: int, positionX: int, positionY: int, parentReference: object, curentCamera: camera, anchor: object, positionFromAnchorX: int, positionFromAnchorY: int,positionFromParentX=0, positionFromParentY=0):
        super().__init__(id, positionX, positionY, parentReference, positionFromParentX, positionFromParentY)

        self.curentCamera = curentCamera
        self.anchor = anchor

        self.positionFromAnchorX = positionFromAnchorX
        self.positionFromAnchorY = positionFromAnchorY
    
    def doYourStuff(self, world, collision_world):
        self.curentCamera.anchorPositionX = self.anchor.positionX + self.positionFromAnchorX
        self.curentCamera.anchorPositionY = self.anchor.positionY + self.positionFromAnchorY

        self.curentCamera.draw(world=world)