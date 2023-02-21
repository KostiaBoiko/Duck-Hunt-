import pygame
from gameplay.gameplay import Gameplay

class Game:
    def __init__(self):
        pygame.display.set_caption("Duck hunt")
        pygame.init()
        Gameplay.game(self)



if __name__ == '__main__':
    game = Game()
    pass
