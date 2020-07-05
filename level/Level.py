
import pygame

from tiles.Specific_Tiles import *
from tiles.Tile import Tile



class Level:
    '''Level/map for game'''

    def __init__(self, game, map_size):
        self.screen = game.screen

        self.map_width, self.map_height = map_size
        #todo = get tile with will be changeable later
        #set tile width and height
        self.tile_width,self.tile_height = Tile.NUM64,Tile.NUM64

        #build map
        self.tiles = self._build_map()

    def _build_map(self):
        map = []
        map.append([FreeSpace(self), Road(self), FreeSpace(self)])
        map.append([FreeSpace(self), Road(self), FreeSpace(self)])
        map.append([FreeSpace(self), Road(self), FreeSpace(self)])
        map.append([FreeSpace(self), Road(self), FreeSpace(self)])
        map.append([FreeSpace(self), Road(self), FreeSpace(self)])
        return map

    def display_map(self):
        for y,val in enumerate(self.tiles):
            for x, tile in enumerate(val):
                tile.blitme((x*self.tile_width, y*self.tile_height))