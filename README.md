# terminalGameEngine
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
You should start by creating game object and map. Map is bassically normal list of strings. Game take 3 arguments world, collision_map (that is basically world map but with arrays in it, not strings).

That's basically on you... What I like is to have some main function and in ther have while loop with some running variable. Then you just need to clear terminal every frame and sleep for the time between the frames.
`
    while (running):
        os.system('clear')

        print(myGame.points)
        myGame.world = [[" "]*width for _ in range(heigth)]

        myGame.do_game_logic()

        sleep(1 / myGame.fps)
`
# Objects
So, this game engine have similiar key features to godot. The main idea is to have parent object that has childs. 
Let's start with the most basic thing you will meet in my example game, the object game. I would say that object game has only. one reallt important functions for you: add_new_child (and also add_new_child_to_the_start, but we will look on that when we will talk about viewports).
The add_new_child function adds new child to the game tree. The childs in game tree are updated every do_game_logic function and they are updating in reverse loop (so the last is updating first). And that's actually all you need to know about the game object!
`#so let's write something:
from src.game.game import game

class myOwnGame(game):
    def __init__(self, world, collision_world, fps):
        super().__init__(world, collision_world, fps)

        self.gravity = 1
        self.points = 0
`
So in this code, we are creating our own game object. we are defining game variables. Game variables can be accessed by the child object, so you will be using them a lot.
If you want to add some functionality to function that's calling every frame, do: 
`
    def do_game_logic(self):
        #your stuff
        return super().do_game_logic()
`

