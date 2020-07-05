from tiles.Tile import Tile


class Road(Tile):
    '''road pipe for moving enemies, tile'''

    def __init__(self, main):
        super().__init__(main)
        super().load_sprite("Route_Straight.png")


class FreeSpace(Tile):
    '''free space for building towers, tile'''

    def __init__(self, main):
        super().__init__(main)
        super().load_sprite("Free_space.png")
        self.buildable = True
