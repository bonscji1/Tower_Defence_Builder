
import pygame
from enemies.Enemy import Enemy
import random

class Enemy1(Enemy):


    def __init__(self, game, spawn_min, spawn_max):
        '''initilization of enemy1'''
        super().__init__(game)
        self.spawn_border = 5
        self.health = 100
        self.speed = 1
        self.damage = 1
        self.image = super().load_sprite("enemy1.png")
        self.rect = self.image.get_rect()

        #this should spawn enemies in random location on the tile
        self.rect.x = random.randint(spawn_min[0]+self.spawn_border, spawn_max[0]-self.spawn_border-self.rect.width)
        self.rect.y = random.randint(spawn_min[1]+self.spawn_border, spawn_max[1]-self.spawn_border-self.rect.height)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
