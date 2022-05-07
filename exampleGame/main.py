from operator import truediv
from re import L
from time import sleep
import os
from src.body.collision_dot import collisionDot

from src.rendering.canvas import canvas
from myAGAME import myOwnGame
from src.body.collisionMap import TileMap

from myOwnPlayer import myOwnPlayer

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
    myGame.add_new_object("player", myOwnPlayer(0, 0, "*", len(myGame.all_objects) + 1, myGame, ["podlaha", "tvojeMama"]))
    myGame.add_new_object("tileMap", TileMap(1, 0, heigth - 2, myGame, "tileMap", "podlaha", 1, 20, "?"))

    myGame.all_objects[1][2].fill_world(collision_world, game_world)

    while (running):
        os.system('clear')

        myGame.canvas = [[" "]*width for _ in range(heigth)]

        myGame.do_game_logic()

        myCanvas.pixels = myGame.canvas
        myCanvas.draw()

        
        sleep(1 / myGame.fps)



main()