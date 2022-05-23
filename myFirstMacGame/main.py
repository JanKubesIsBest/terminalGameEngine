from operator import truediv
from re import L
from time import sleep
import os
from src.rendering.camera import camera
from src.body.collision_dot import collisionDot

from myAGAME import myOwnGame
from myOwnTarget import myOwnTarget

from src.rendering.canvas import canvas
from src.body.collisionMap import TileMap

from myOwnPlayer import myOwnPlayer
from src.body.viewport import viewport

running = True
width = 30
heigth = 10

array = [[] for _ in range(width)]
game_world = [[" "]*width for _ in range(heigth)]
collision_world = [[[collisionDot(None, None, None, None, None)] for _ in range(width)] for _ in range(heigth)]


myCanvas = canvas(width, heigth, game_world)
myGame = myOwnGame(game_world, collision_world, 5)

def main():
    #main function, everthing starts here
    print("game started...")
    
    #adding rooted objects
    myGame.add_new_child("tileMap", TileMap(1, 0, heigth - 2, myGame, "tileMap", "podlaha", 1, 20, "?"))

    myGame.all_objects[0][2].fill_world(collision_world, game_world)

    myGame.add_new_child("player", myOwnPlayer(0, 0, "*", len(myGame.all_objects) + 1, myGame, ["podlaha", "tvojeMama"]))
    myGame.add_new_child("target", myOwnTarget(6, 6, "T", len(myGame.all_objects) + 1, myGame, ["bullet"]))

    myGame.add_new_child_to_the_start("viewPortForPlayer", viewport(2, 0, 0, myGame, camera(7, 7), myGame.all_objects[1][2], -2, -2))


    while (running):
        os.system('clear')

        print(myGame.points)
        myGame.world = [[" "]*width for _ in range(heigth)]

        myGame.do_game_logic()

        sleep(1 / myGame.fps)



main()