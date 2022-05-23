

class game:
    def __init__(self, world, collision_world, fps,):
        self.world = world

        self.all_objects = []

        self.keyboard_signals = []

        self.collision_world = collision_world

        self.fps = fps


    def do_game_logic(self):

        self.update_all_rooted_objects()

    def update_all_rooted_objects(self):

        for x in range(len(self.all_objects) - 1, -1, -1):
            self.all_objects[x][2].update(self.world, self.collision_world)

    def add_new_child(self, object_name, object_reference):
        self.all_objects.append([(len(self.all_objects) + 1), object_name, object_reference])
    def add_new_child_to_the_start(self, object_name, object_reference):
        self.all_objects.insert(0, [(len(self.all_objects) + 1), object_name, object_reference])