from src.game.game import game

class myOwnGame(game):
    def __init__(self, canvas, collision_world, fps):
        super().__init__(canvas, collision_world, fps)

        self.gravity = 1
