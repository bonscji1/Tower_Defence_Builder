from tiles.Tile import Tile
import enum

class Directions(enum.Enum):
    UP = 1
    Right = 2
    Down = 3
    Left = 4


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

    def __init__(self, main, location):
        super().__init__(main)
        super().load_sprite("portal.png")
        self.spawn_min = (location[0]*super().NUM64, location[1]*super().NUM64)
        self.spawn_max = (self.spawn_min[0] + super().NUM64, self.spawn_min[1] + super().NUM64)
        self.IN = Directions.UP
        self.OUT = Directions.Down

class TownUM(Tile):
    '''end destination of enemies, go from up to middle'''
    #todo add colision model to reduce lives

    def __init__(self, main, location):
        super().__init__(main)
        super().load_sprite("town.png")
        self.rect = self.image.get_rect()#returns 0,0,64,64 aka size of this block
        self.rect[0] += location[0]*super().NUM64
        self.rect[1] += location[1]*super().NUM64+self.rect.height/10#correction for the sprite, thez can move a little bit in
        self.IN = Directions.UP
        self.OUT = Directions.Down
