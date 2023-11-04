import os
from time import sleep
from src.body.collision_dot import CollisionDot
from src.game.game import Game
from src.rendering.canvas import Canvas


def main():
    # Main function, everything starts and ends here.
    print("game started...")

    running = True
    width = 30
    height = 10

    game_world = [[" "] * width for _ in range(height)]
    game_world[1][1] = "f"
    collision_world = [[[CollisionDot(None, None, None, None, None)] for _ in range(width)] for _ in range(height)]

    myCanvas = Canvas(width, height, game_world)
    myGame = Game(game_world, collision_world, 10)

    while (running):
        os.system('clear')

        myGame.world = [[" "] * width for _ in range(height)]

        myGame.do_game_logic()

        myCanvas.pixels = myGame.canvas
        myCanvas.draw()

        sleep(1 / myGame.fps)


main()
