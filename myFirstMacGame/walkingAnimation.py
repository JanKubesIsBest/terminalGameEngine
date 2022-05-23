from src.design.animation import animation 

class walkingAnimation(animation):
    def __init__(self, animationName):
        super().__init__(animationName)

        self.animation = [
            [
            [" ", "*", " "],
            [" ", "*", " "],
            ["*", "*", "*"],
            ],
            [
            [" ", "*", " "],
            [" ", "*", " "],
            ["*", " ", "*"],
            ],
            [
            [" ", "*", " "],
            ["*", "*", "*"],
            [" ", " ", " "],
            ],
            [
            [" ", "*", " "],
            [" ", "*", " "],
            ["*", " ", "*"],
            ],
        ]
