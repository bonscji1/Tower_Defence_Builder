from tiles.Tile import Tile
import enum

class Directions(enum.Enum):
    UP = 1
    Right = 2
    Down = 3
    Left = 4
    Middle = 5


class RoadUD(Tile):
    '''road pipe for moving enemies, tile, road goes from Up to Down'''

    def __init__(self, main):
        super().__init__(main)
        super().load_sprite("route_straight.png")
        self.IN = Directions.UP
        self.OUT = Directions.Down



class FreeSpace(Tile):
    '''free space for building towers, tile'''

    def __init__(self, main):
        super().__init__(main)
        super().load_sprite("free_space.png")
        self.buildable = True

class SpawnMD(Tile):
    '''tile for spawning enemies, spawn in middle and go down'''

    def __init__(self, main):
        super().__init__(main)
        super().load_sprite("portal.png")
        self.IN = Directions.Middle
        self.OUT = Directions.Down
