

class game:
    def __init__(self, canvas, collision_world,  fps):
        self.canvas = canvas

        self.all_objects = []

        self.keyboard_signals = []

        self.collision_world = collision_world

        self.fps = fps

    def do_game_logic(self):

        self.update_all_rooted_objects()

    def update_all_rooted_objects(self):

        for x in self.all_objects:
            x[2].update(self.canvas, self.collision_world)

    def add_new_object(self, object_name, object_reference):
        self.all_objects.append([(len(self.all_objects) + 1), object_name, object_reference])