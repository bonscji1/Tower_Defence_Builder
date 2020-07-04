from tiles.Tile import Tile

class Road(Tile):
    '''road pipe for moving enemies, tile'''

    def __init__(self):
        super().__init__()
        super().load_sprite("road.png")

