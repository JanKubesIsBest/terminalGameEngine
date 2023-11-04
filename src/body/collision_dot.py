from src.body.body.bodyClass import Body


class CollisionDot(Body):
    def __init__(self, id: int, positionX: int, positionY: int, parentReference: object, group: str):
        super().__init__(id, positionX, positionY, parentReference)

        self.group = group
