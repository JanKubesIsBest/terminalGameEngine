from src.body.body.bodyClass import body

class collisionDot(body):
    def __init__(self, id: int, positionX: int, positionY: int, parentReference: object, group: str):
        super().__init__(id, positionX, positionY, parentReference)

        self.group = group 

