import pygame

class Drawer:

    def __init__(self):
        SCREEN_WIDTH = 720
        SCREEN_HEIGHT = 480

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags=pygame.SCALED)
        background = pygame.image.load("assets/game/game_back.png").convert_alpha()
        self.screen.blit(background, (0, 0))

    def menu(self):

        pass
    def start_menu(self):
        background = pygame.image.load('assets/menu/background.png').convert_alpha()
        self.screen.blit(background,(0,0))
        pass
