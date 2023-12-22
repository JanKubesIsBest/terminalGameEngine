# TerminalGameEngine
Made by me when I was 14 years old, it is not updated anymore.

Game engine for terminal games

# How to create game?
Download the src folder and start experiencing my delicious code...
Too lazy to write a documentation... Maybe later.

# What is there:
Basic terminal animation, childs and parent system, collision map and detection shape and some other stuff...

# What is still missing and will be added (I hope):
Camera object (currently I am drawing whole map), more collision functions and then I will try to create shooting example game, but we will see about that.

# Basic documentation

# How to start
The easiest way to start is this:
 
```
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
```

The most important parts of this are:
- Initialization of the game object. That takes game_world variable, which is an array of strings. Collision_world variable which has same dimensions as world, but is filled with collision dots.
- Fps -> self explanatory.
- Canvas -> draws everything.
- myGame.do_game_logic() calls every child of game class to do their logic (scroll more for details). Additionally you can add your own logic into it. 
# Objects
So, this game engine have similiar key features to godot. The main idea is to have parent object that has childs. 
Let's start with the most basic thing you will meet in my example game, the object game. I would say that object game has only. one reallt important functions for you: add_new_child (and also add_new_child_to_the_start, but we will look on that when we will talk about viewports).
The add_new_child function adds new child to the game tree. The childs in game tree are updated every do_game_logic function and they are updating in reverse loop (so the last is updating first). And that's actually all you need to know about the game object!
```
#so let's write something:
from src.game.game import game

class myOwnGame(game):
    def __init__(self, world, collision_world, fps):
        super().__init__(world, collision_world, fps)

        self.gravity = 1
        self.points = 0
```
So in this code, we are creating our own game object. we are defining game variables. Game variables can be accessed by the child object, so you will be using them a lot.
If you want to add some functionality to function that's calling every frame, do: 
```
    def do_game_logic(self):
        #your stuff
        return super().do_game_logic()
```

