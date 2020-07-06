
import pygame
import sys
from pygame.sprite import Sprite

class Tile(Sprite):
    '''Parent class for all tiles'''
    #TODO: change this to modular later
    NUM64 = 64

    def __init__(self, main):
        super().__init__()
        #todo:change
        self.width: int = self.NUM64 #in bits
        self.height: int = self.NUM64


        self.buildable = False
        self.screen = main.screen
        self.sprite = None

    def load_sprite(self, name):
        try:
            self.sprite = pygame.image.load("resources/sprites/"+name)
        except  pygame.error:
            print(f"No such file as {name} in resources")
            print("Terminating program")
            sys.exit(1)

    def blitme(self, location):
        '''draw at location'''
        self.screen.blit(self.sprite, location)
