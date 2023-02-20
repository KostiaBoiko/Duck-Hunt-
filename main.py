import pygame


class Game:
    def __init__(self):
        pygame.display.set_caption("Duck hunt")
        pygame.init()
        SCREEN_WIDTH = 720
        SCREEN_HEIGHT = 480

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags=pygame.SCALED)
        background = pygame.image.load("assets/game/game_back.png").convert_alpha()
        run = True

        while run:
            screen.blit(background,(0,0))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_ESCAPE:
                       pass
                if event.type == pygame.QUIT:
                    run = False
        pygame.display.update()



if __name__ == '__main__':
    game = Game()
    pass