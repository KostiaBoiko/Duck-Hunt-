import pygame
from drawer.drawer import Drawer
class Gameplay:

    def game(self):
        run = True
        draw = Drawer()
        while run:
            draw.start_menu()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_ESCAPE:

                        pass
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()