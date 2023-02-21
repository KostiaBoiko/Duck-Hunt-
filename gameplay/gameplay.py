import pygame
from drawer.drawer import Drawer
from drawer.objects import Objects
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
                    else:
                        obg = Objects()
                        obg.add_enemies_to_list()
                        obg.enemy_movement()

                #controls
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.type == pygame.K_ESCAPE:
                            pass
                    if event.type == pygame.QUIT:
                        run = False
                pygame.display.update()

    def actions(x):
        pass