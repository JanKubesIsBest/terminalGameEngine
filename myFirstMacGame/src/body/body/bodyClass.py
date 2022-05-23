class body:
    def __init__(self, id: int, positionX: int, positionY: int, parentReference: object, positionFromParentX = 0, positionFromParentY = 0):
        self.positionX = positionX
        self.positionY = positionY

        self.childs = []

        self.id = id

        self.defaultSkin = "#" 

        self.parentReference = parentReference

        self.positionFromParentX = positionFromParentX
        self.positionFromParentY = positionFromParentY
    
    def update(self, world, collision_world):
        
        self.doYourStuff(world, collision_world)
        self.update_all_childs(world, collision_world)

        if self.defaultSkin != "" and self.positionY < len(world) and self.positionX < len(world[self.positionY]) and self.positionY > 0 and self.positionX > 0:
            world[self.positionY][self.positionX] = self.defaultSkin

    def update_all_childs(self, world, collision_world):
        for x in self.childs:
            self.doStuffWithUpdatedChild(x[2])
            x[2].update(world, collision_world)
    
    def add_new_child(self, object_name, object_reference):
        self.childs.append([(len(self.childs) + 1), object_name, object_reference])
        
    def doStuffWithUpdatedChild(self, child):
        child.positionX = self.positionX + child.positionFromParentX
        child.positionY = self.positionY + child.positionFromParentY
    
    def doYourStuff(self, world, collision_world):
        pass
    

    def draw(self):
        for x in self.childs:
            x[2].draw()