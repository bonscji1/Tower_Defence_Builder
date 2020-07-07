
import pygame
import json
from pygame.sprite import Group

from tiles.Specific_Tiles import *
from tiles.Tile import Tile

from enemies.Specific_Enemy import *
from enemies.Enemy import Enemy

#TODO: CHANGE
LEVEL_NAME = "Level1"
ENEMY_NUMBER = 10



class Level:
    '''Level/map for game'''

    def __init__(self, game, map_size):
        self.screen = game.screen

        self.map_width, self.map_height = map_size
        #todo = get tile with will be changeable later
        #set tile width and height
        self.tile_width,self.tile_height = Tile.NUM64,Tile.NUM64

        tiles_in_X = self.map_width/self.tile_width
        tiles_in_y = self.map_height/self.tile_height

        self.level_design = self._load_level(LEVEL_NAME)

        # enemies and spawns
        self.spawns = Group()
        self.enemies = Group()
        self.wave1 = 0

        #build map
        self.tiles = self._build_map(int(tiles_in_X), int(tiles_in_y))



    def _build_map(self,in_x,in_y):
        map_level = []
        for positionY in range(in_y):
            field = []
            for positionX in range(in_x):
                tile_type = self.level_design[positionY][positionX]

                if tile_type == "RoadUD":
                    field.append(RoadUD(self))
                elif tile_type == "FreeSpace":
                    field.append(FreeSpace(self))
                elif tile_type == "SpawnMD":
                    spawn = SpawnMD(self, (positionX, positionY))
                    field.append(spawn)
                    self.spawns.add(spawn)

                elif tile_type == "TownUM":
                    field.append(TownUM(self))

            map_level.append(field)
        return map_level

    def _load_level(self,name):
        path = "resources/levels/" + name
        try:
            with open(path)as f:
                level = json.load(f)
        except FileNotFoundError:
            return None
        return level

    def save_level(self):
        path = "resources/levels/"+LEVEL_NAME

        with open(path, 'w') as f:
            json.dump(self.level_design, f)


    def display_map(self):
        for y,val in enumerate(self.tiles):
            for x, tile in enumerate(val):
                tile.blitme((x*self.tile_width, y*self.tile_height))

    def spawn_enemy(self):
        if self.wave1 < ENEMY_NUMBER:
            self.wave1+=1
            for spawn in self.spawns.sprites():
                self.enemies.add(Enemy1(self,spawn.spawn_min, spawn.spawn_max))

    def move_enemies(self):
        self.enemies.update((0,1))
        self.enemies.draw(self.screen)