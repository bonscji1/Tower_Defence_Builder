
import pygame
import sys
from pygame.sprite import Sprite

class Enemy(Sprite):
    '''base enemy class'''

    def __init__(self, main):
        super().__init__()
        self.screen = main.screen
        self.health = 0
        self.speed = 0
        self.damage = 0
        self.image = None
        self.rect = None
        self.x = 0
        self.y = 0
        #todo add admor, magic armon and regen and yada yada

    def load_sprite(self, name):
        try:
            sprite = pygame.image.load("resources/enemies/"+name)
        except  pygame.error:
            print(f"No such file as {name} in resources")
            print("Terminating program")
            sys.exit(1)
        return sprite

    def update(self,vector):
        '''move enemy in the indicated direction'''
        # this is here in case of float speeds
        self.x += vector[0]*self.speed
        self.y += vector[1] * self.speed
        self.rect.x = self.x
        self.rect.y = self.y



    def blitme(self):
        '''draw at location'''
        self.screen.blit(self.image, self.rect)
