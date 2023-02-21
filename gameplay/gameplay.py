import pygame
from drawer.drawer import Drawer
from drawer.objects import Objects
class Gameplay:

    def game(self):
        gameplay = True
        running = True
        enemy = Objects()
        enemy.bg()
        enemy.add_enemies_to_list()
        while running:
            if gameplay:
                pass
            pygame.display.update()

    def actions(x):
        pass