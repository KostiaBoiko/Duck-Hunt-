import pygame
from drawer.drawer import Drawer
class Gameplay:

    def game(self):
        gameplay = True
        run = True
        is_game_pause = True
        drawer = Drawer()
        if gameplay:
            while run:
                if drawer.draw_start_menu() == False:
                    if drawer.draw_menu(is_game_pause) == False:
                        is_game_pause = False
                        print('sun of wqweqweqw')

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.type == pygame.K_ESCAPE:
                            pass
                    if event.type == pygame.QUIT:
                        run = False
                pygame.display.update()

    def actions(x):
        pass