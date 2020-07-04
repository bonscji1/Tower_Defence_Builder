from tiles.Tile import Tile

class Road(Tile):
    '''road pipe for moving enemies, tile'''

    def __init__(self,main, location):
        super().__init__(main,location)
        super().load_sprite("Route_Straight.png")




