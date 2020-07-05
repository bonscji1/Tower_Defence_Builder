
import pygame
from tiles.Road import Road


class Level:
    '''Level/map for game'''

    def __init__(self, game, map_size):
        self.screen = game.screen

        self.map_width, self.map_height = map_size

        self.tiles = pygame.sprite.Group()

        road_tile = Road(self, (0, 0))  # 1 for now
        self.tiles.add(road_tile)

    def display_map(self):
        for tile in self.tiles.sprites():
            tile.blitme()