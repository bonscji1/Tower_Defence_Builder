
import pygame
import sys
from tiles.Road import Road


class Tower_Defence_Builder:
    '''Main class for mz application'''

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tower Defence Builder")

        #display screen
        self.screen_size = self.screen_width, self.screen_height = 640, 320


        self.screen = pygame.display.set_mode(self.screen_size)

        self.background_color = (0,0,0)

        self.tiles= pygame.sprite.Group()

        road_tile = Road(self, (0,0))  # 1 for now
        self.tiles.add(road_tile)




    def _update_screen(self):
        '''re-draw screen'''
        self.screen.fill(self.background_color)

        self._build_map()

        pygame.display.flip()

    def _build_map(self):
        for tile in self.tiles.sprites():
            tile.blitme()

    def run(self):
        '''Main loop'''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self._update_screen()

if __name__ == "__main__":
    main = Tower_Defence_Builder()
    main.run()