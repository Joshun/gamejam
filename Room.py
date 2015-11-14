class Room(object):
    """Base class for a Room"""
    def __init__(self, tiled_map):
        self.tiled_map = tiled_map
        # self.interative_objects = i_objs

    def draw(self, screen):
        self.tiled_map.draw(screen)

    def update(self,screen):
        pass