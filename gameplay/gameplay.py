import pygame
from drawer.drawer import Drawer
class Gameplay:

    def game(self):
        run = True
        Drawer.drawbg(self)
        while run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_ESCAPE:
                        pass
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()