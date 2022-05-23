from src.game.game import game

class myOwnGame(game):
    def __init__(self, world, collision_world, fps):
        super().__init__(world, collision_world, fps)

        self.gravity = 1
        self.points = 0
