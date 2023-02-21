import pygame
#from drawer import Drawer
class Objects:

    def __init__(self):
        SCREEN_WIDTH = 720
        SCREEN_HEIGHT = 480
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags=pygame.SCALED)

        self.plane_1 = pygame.transform.scale(pygame.image.load('assets/game/plane_1.png').convert_alpha(), [128, 64])
        self.plane_2 = pygame.transform.scale(pygame.image.load('assets/game/plane_2.png').convert_alpha(), [128, 64])
        self.plane_3 = pygame.transform.scale(pygame.image.load('assets/game/plane_3.png').convert_alpha(), [128, 64])
        self.enemy_list_in_game = []
        self.background = pygame.image.load("assets/game/game_back.png").convert_alpha()

    def bg(self):
        #background = pygame.image.load("assets/game/game_back.png").convert_alpha()
        self.screen.blit(self.background, (0, 0))

    def add_enemies_to_list(self):
        self.enemy_list_in_game.append(self.plane_1.get_rect(topleft=(300, 200)))
        self.screen.blit(self.plane_1, (200, 200))
