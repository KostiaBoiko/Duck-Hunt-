import pygame
clock = pygame.time.Clock()
class Drawer:

    def bg(self):
        SCREEN_WIDTH = 720
        SCREEN_HEIGHT = 480

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags=pygame.SCALED)
        background = pygame.image.load("assets/game/game_back.png").convert_alpha()
        self.screen.blit(background, (0, 0))
        self.pause = True
        self.start_screen = True
        self.mouse = pygame.mouse.get_pos()

    def draw_start_menu(self):
        self.mouse = pygame.mouse.get_pos()
        self.screen.fill('grey')
        if self.start_screen:
            background = pygame.image.load("assets/menu/background.png").convert_alpha()
            start_game_button = pygame.image.load("assets/menu/button_StartGame.png").convert_alpha()
            self.screen.blit(background,(0,0))
            self.screen.blit(start_game_button, (168, 154))

            start_game_button_rect = start_game_button.get_rect(topleft=(168, 154))

            if start_game_button_rect.collidepoint(self.mouse) and pygame.mouse.get_pressed()[0]:
                print("fuck")
                self.start_screen = False
        else:
            return False
    def draw_menu(self, pause):
        if pause:
            background = pygame.image.load("assets/menu/background.png").convert_alpha()
            play_game_button = pygame.image.load("assets/menu/button_Play.png").convert_alpha()
            settings_game_button = pygame.image.load("assets/menu/button_Settings.png").convert_alpha()
            exit_game_button = pygame.image.load("assets/menu/button_Exit.png").convert_alpha()
            self.screen.blit(background,(0,0))
            self.screen.blit(play_game_button, (255, 72))
            self.screen.blit(settings_game_button, (255, 147))
            self.screen.blit(exit_game_button, (255, 368))

            play_game_button_rect = play_game_button.get_rect(topleft=(255, 72))
            settings_game_button_rect = settings_game_button.get_rect(topleft=(255, 147))
            exit_game_button_rect = exit_game_button.get_rect(topleft=(255, 368))

            if play_game_button_rect.collidepoint(self.mouse) and pygame.mouse.get_pressed()[0]:
                return False
            elif settings_game_button_rect.collidepoint(self.mouse) and pygame.mouse.get_pressed()[0]:
                print("settings")
            elif exit_game_button_rect.collidepoint(self.mouse) and pygame.mouse.get_pressed()[0]:
                pygame.quit()


