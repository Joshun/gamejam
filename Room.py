class Room(object):
  """Base class for a Room"""
  def __init__(self, tiled_map):
    self.tiled_map = tiled_map

  def draw(self):
    pass

  def update(self):
    pass
    