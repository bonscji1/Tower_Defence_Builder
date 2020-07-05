
import pygame
import sys
from level.Level import Level


class Tower_Defence_Builder:
    '''Main class for mz application'''

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tower Defence Builder")

        # display screen
        self.screen_size = self.screen_width, self.screen_height = 640, 320

        self.screen = pygame.display.set_mode(self.screen_size)

        self.background_color = (0,0,0)

        self.level = Level(self,self.screen_size)


    def _update_screen(self):
        '''re-draw screen'''
        self.screen.fill(self.background_color)

        self.level.display_map()

        pygame.display.flip()



    def run(self):
        '''Main loop'''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.level.save_level()
                    sys.exit()

            self._update_screen()

if __name__ == "__main__":
    main = Tower_Defence_Builder()
    main.run()