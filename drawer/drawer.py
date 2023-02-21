import pygame

class Drawer:

    def drawbg(self):
        SCREEN_WIDTH = 720
        SCREEN_HEIGHT = 480
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags=pygame.SCALED)
        background = pygame.image.load("assets/game/game_back.png").convert_alpha()
        screen.blit(background, (0, 0))



