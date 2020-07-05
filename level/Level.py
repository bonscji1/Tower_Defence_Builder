
import pygame

from tiles.Road import Road
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
        self.tiles = []
        self.tiles.append([Road(self), Road(self)])
        self.tiles.append([Road(self), Road(self)])
        self.tiles.append([Road(self)])


    def display_map(self):
        for x,val in enumerate(self.tiles):
            for y, tile in enumerate(val):
                tile.blitme((x*self.tile_width, y*self.tile_height))